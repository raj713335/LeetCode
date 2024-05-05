# https://leetcode.com/problems/custom-interval/description/

const idMap = {}

function* infiniteGenerator() {
  let index = 0;

  while (true) {
    yield index++;
  }
}

const generateId = infiniteGenerator()

function customInterval(fn: Function, delay: number, period: number): number {
    let count = 0
    const id = generateId.next().value as number
    function createCustomInterval() {
        const interval = setTimeout(() => {
            fn()
            createCustomInterval()
        }, delay + period*count)
        idMap[id] = interval
        count++
    }

    createCustomInterval()
    return id
}

function customClearInterval(id: number): void {
    clearInterval(idMap[id])
}
