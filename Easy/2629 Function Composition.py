# https://leetcode.com/problems/function-composition/description/

type F = (x: number) => number;

function compose(functions: F[]): F {
return function(input: number): number {
let result = input;
    for (let i = functions.length - 1; i >= 0; i--) {
        result = functions[i](result);
    }
    return result;
}};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
