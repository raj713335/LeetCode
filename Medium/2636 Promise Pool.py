# https://leetcode.com/problems/promise-pool/description/


type F = () => Promise<any>;

function promisePool(functions: F[], n: number): Promise<any> {

    const iterator = functions[Symbol.iterator]()
    
     let worker = async (): Promise<any> => {
        for (const func of iterator) {
            await func();
        }
     }

    let workers: Promise<any>[] = [];
    while (n-- > 0) {
        workers.push(worker());
    }

    return Promise.all(workers);
    
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
