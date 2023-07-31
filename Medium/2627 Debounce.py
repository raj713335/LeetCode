# https://leetcode.com/problems/debounce/description/

type F = (...p: any[]) => any

function debounce(fn: F, t: number): F {
    let timeout: ReturnType<typeof setTimeout>
    return (...args) => {
        clearTimeout(timeout)
        timeout = setTimeout(() => fn(...args), t)
        
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */
