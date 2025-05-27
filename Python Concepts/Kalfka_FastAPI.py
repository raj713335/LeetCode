# Minimal but complete example of how to connect **FastAPI** to **Kafka** using both a **producer (publisher)** and a **consumer (subscriber)** with `aiokafka` for asynchronous Kafka operations.

---

## ✅ Requirements

Install the dependencies:

```bash
pip install fastapi uvicorn aiokafka
```

You’ll also need a running Kafka instance. You can use Docker:

```bash
docker run -d --name kafka -p 9092:9092 -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
  --network=host \
  bitnami/kafka:latest
```

---

## 📦 FastAPI Kafka Example

### `main.py`

```python
from fastapi import FastAPI, BackgroundTasks
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio
import json

KAFKA_TOPIC = "my_topic"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

app = FastAPI()
producer = None


@app.on_event("startup")
async def startup_event():
    global producer
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    asyncio.create_task(consume_messages())


@app.on_event("shutdown")
async def shutdown_event():
    global producer
    await producer.stop()


@app.post("/publish/")
async def publish(message: dict):
    value = json.dumps(message).encode("utf-8")
    await producer.send_and_wait(KAFKA_TOPIC, value=value)
    return {"status": "Message published"}


async def consume_messages():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="fastapi-group"
    )
    await consumer.start()
    try:
        async for msg in consumer:
            data = json.loads(msg.value.decode("utf-8"))
            print(f"Received message: {data}")
    finally:
        await consumer.stop()
```

---

## ▶️ Run the App

```bash
uvicorn main:app --reload
```

---

## 📬 Test the Publisher

Use `curl` or Postman to send messages:

```bash
curl -X POST "http://127.0.0.1:8000/publish/" -H "Content-Type: application/json" -d '{"text": "hello kafka"}'
```

---

## 🧠 Notes

* **Producer**: Sends JSON messages to Kafka.
* **Consumer**: Runs as a background task and prints received messages.
* **Asynchronous**: Both producer and consumer are async, making it scalable.

