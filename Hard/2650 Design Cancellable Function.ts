# https://leetcode.com/problems/design-cancellable-function/description/

function cancellable<T>(generator: Generator<Promise<any>, T, unknown>): [() => void, Promise<T>] {

    let cancel: () => void;
    const cancelPromise = new Promise<never>((_, reject) => {
        cancel = () => reject("Cancelled");
    });
    // Every Promise rejection has to be caught.
    cancelPromise.catch(() => {});

    const promise = (async (): Promise<T> => {
        let next = generator.next();
        while (!next.done) {
        try {
            next = generator.next(await Promise.race([next.value, cancelPromise]));
        } catch (e) {
            next = generator.throw(e);
        }
        }
        return next.value;
    })();

    return [cancel, promise];
    
};

/**
 * function* tasks() {
 *   const val = yield new Promise(resolve => resolve(2 + 2));
 *   yield new Promise(resolve => setTimeout(resolve, 100));
 *   return val + 1;
 * }
 * const [cancel, promise] = cancellable(tasks());
 * setTimeout(cancel, 50);
 * promise.catch(console.log); // logs "Cancelled" at t=50ms
 */
