# https://leetcode.com/problems/group-by/description/

declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function(fn) {
    const hash = {}
    for (let item of this){
        const key = fn(item)
        hash[key] ||= []
        hash[key].push(item)
    }
    return hash
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
