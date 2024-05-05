# https://leetcode.com/problems/delay-the-resolution-of-each-promise/description/


type Fn = () => Promise<any>

function delayAll(functions: Fn[], ms: number): Fn[] {

    return functions.map((elem) => () => new Promise((resolve) => {
        setTimeout(() => {
            resolve(elem())
        }, ms);
    }))
    
};
