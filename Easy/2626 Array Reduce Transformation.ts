// https://leetcode.com/problems/array-reduce-transformation/description/

type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    
    let sumx : number = init || 0;

    for(let i=0;i<nums.length;i++){ 
        sumx = fn(sumx, nums[i]);
    }

    return sumx;        

};
