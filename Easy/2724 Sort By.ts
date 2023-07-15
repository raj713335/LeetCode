# https://leetcode.com/problems/sort-by/description/

function sortBy(arr: any[], fn: Function): any[] {
    return arr.sort((a, b) => fn(a) - fn(b));
};
