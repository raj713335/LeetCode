# https://leetcode.com/problems/partial-function-with-placeholders/description/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Fn = (...args: JSONValue[]) => JSONValue

function partial(fn: Fn, args: JSONValue[]): Fn {
    
    return function(...restArgs) {

        const currentRestArgs = [...restArgs];
        const appliedArgs = args.map((arg) => {
            if (arg === '_' && currentRestArgs.length) {
                return currentRestArgs.shift();
            }
            return arg;
        });
        return fn(...appliedArgs, ...currentRestArgs);
        
    }
};
