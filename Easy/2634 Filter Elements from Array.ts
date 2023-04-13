// https://leetcode.com/problems/filter-elements-from-array/description/

function filter(arr: number[], fn: (n: number, i: number) => any): number[] {

    let array = [];

    for (let i=0; i<arr.length; i++) {
        if (fn(arr[i], i)) {
            array.push(arr[i]);
        }
    }

    return array;
};
