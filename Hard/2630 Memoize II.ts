# https://leetcode.com/problems/memoize-ii/description/


type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    
    const idPool = new Map<unknown, number>()
    const cache: Map<string, ReturnType<Fn>> = new Map()
    return function (...args: Parameters<Fn>): ReturnType<Fn> {
        const key = args.map(getId).join(',')
        if (cache.has(key)) {
        return cache.get(key)!
        }
        const res = fn(...args)
        cache.set(key, res)
        return res
    }

    function getId(o: unknown): number {
        if (idPool.has(o)) {
        return idPool.get(o)!
        }
        const id = idPool.size
        idPool.set(o, id)
        return id
    }
    
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
