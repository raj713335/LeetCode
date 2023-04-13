// https://leetcode.com/problems/apply-transform-over-each-element-in-array/description/


function map(arr: number[], fn: (n: number, i: number) => number): number[] {

    for (let i=0; i<arr.length; i++){
        arr[i] = fn(arr[i], i);
    }
    return arr;

};
