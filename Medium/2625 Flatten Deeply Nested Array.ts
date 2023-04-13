// https://leetcode.com/problems/flatten-deeply-nested-array/description/


type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr:  MultiDimensionalArray, n: number):  MultiDimensionalArray {

    return arr.flat(n);
    
};
