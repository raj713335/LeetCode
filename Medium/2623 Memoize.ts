# https://leetcode.com/problems/memoize/description/


type Fn = (...params: number[]) => number

function memoize(fn: Fn): Fn {
    
    let map = new Map();
    let ans = function(...params:any):any
    {
        let input:string = params.join(",").toString();
        if(map.get(input) == undefined)
        {
            map.set(input,fn(...params));
        }
        return map.get(input);
        
    }

    return ans;
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
