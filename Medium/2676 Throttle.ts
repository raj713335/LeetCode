# https://leetcode.com/problems/throttle/description/


type F = (...args: number[]) => void;
type Timeout = ReturnType<typeof setTimeout>;

function throttle(fn: F, t: number): F {
    
    let lastExecTime = 0;
    let ref: NodeJS.Timeout | null = null;
    let curArgs: any[] | null = null;

    return function (...args) {
        const now = Date.now();

        if (now - lastExecTime >= t) {
            fn(...args);
            lastExecTime = now;
        } else {
            if (ref) clearTimeout(ref);

            ref = setTimeout(() => {
                fn(...(curArgs || []));
                lastExecTime = Date.now();
            }, t - (now - lastExecTime));

            curArgs = args;
        }
    }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
