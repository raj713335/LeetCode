# https://leetcode.com/problems/cache-with-time-limit/description/


class TimeLimitedCache {

    cache: Map<number, any>;
    
    constructor() {
        this.cache = new Map();
    }
    
    set(key: number, value: number, duration: number): boolean {

        let existed: boolean = this.cache.has(key);
        if (existed) 
            clearTimeout(this.cache.get(key).ref);
        this.cache.set(key, {
            value,
            ref: setTimeout(() => {
                this.cache.delete(key);
            }, duration)
        });
        return existed;
        
    }
    
    get(key: number): number {
        return this.cache.has(key) ? this.cache.get(key).value : -1;
    }
    
    count(): number {
        return this.cache.size;
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */
