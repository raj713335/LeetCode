import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

def health_check(endpoints, timeout=5):
    """
    Perform a health check on multiple API endpoints concurrently.
    
    Args:
        endpoints (list): A list of API endpoint URLs (strings).
        timeout (int): Timeout for each request in seconds.

    Returns:
        dict: A dictionary mapping each endpoint to its status and response time.
    """
    results = {}

    def check(url):
        try:
            response = requests.get(url, timeout=timeout)
            return url, {
                "status_code": response.status_code,
                "ok": response.ok,
                "response_time": response.elapsed.total_seconds()
            }
        except requests.RequestException as e:
            return url, {
                "status_code": None,
                "ok": False,
                "error": str(e)
            }

    with ThreadPoolExecutor(max_workers=len(endpoints)) as executor:
        future_to_url = {executor.submit(check, url): url for url in endpoints}
        for future in as_completed(future_to_url):
            url, result = future.result()
            results[url] = result

    return results

# Example usage
if __name__ == "__main__":
    endpoints = [
        "https://api.github.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts",
        "https://does-not-exist.typicode.com"  # for testing error handling
    ]

    result = health_check(endpoints)
    for url, info in result.items():
        print(f"{url}: {info}")
