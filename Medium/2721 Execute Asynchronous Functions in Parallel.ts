# https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/submissions/1250031071/


type Fn<T> = () => Promise<T>

function promiseAll<T>(functions: Fn<T>[]): Promise<T[]> {

    let resolvedPromises = [];
    let resolvedCounter = 0;

    return new Promise((resolve, reject) => {
        functions.forEach((item, index) => {
            item()
                .then(result => {
                    resolvedPromises[index] = result;
                    resolvedCounter++;
                    if (resolvedCounter === functions.length) {
                        resolve(resolvedPromises);
                    }
                })
                .catch(err => reject(err))
        })
    })
    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
