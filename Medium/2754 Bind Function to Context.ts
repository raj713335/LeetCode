# https://leetcode.com/problems/bind-function-to-context/description/

type Fn = (...args) => any

declare global {
    interface Function {
        bindPolyfill(obj: Record<any, any>): Fn;
    }
}

Function.prototype.bindPolyfill = function(obj): Fn {
    return this.bind(obj)
    
}
