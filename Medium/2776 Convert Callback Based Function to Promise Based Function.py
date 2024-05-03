# https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/description/


type CallbackFn = (
    next: (data: number, error: string) => void, 
    ...args: number[]
) => void
type Promisified = (...args: number[]) => Promise<number>

function promisify(fn: CallbackFn): Promisified {
    
    return async (...args) => new Promise((resolve, reject) => {
        const callback = (data: number, err: string | Error) => {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        };
        return fn(callback, ...args);
    }); 
};

/**
 * const asyncFunc = promisify(callback => callback(42));
 * asyncFunc().then(console.log); // 42
 */
