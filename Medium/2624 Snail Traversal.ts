# https://leetcode.com/problems/snail-traversal/description/


declare global {
    interface Array<T> {
        snail(rowsCount: number, colsCount: number): number[][];
    }
}

Array.prototype.snail = function(rowsCount: number, colsCount: number): number[][] {
    return rowsCount * colsCount !== this.length ? [] : this.reduce((acc, num, i) =>
         (acc[Math.floor(i / rowsCount) % 2 ? 
            rowsCount - i % rowsCount - 1 : 
            i % rowsCount][Math.floor(i / rowsCount)] = num) 
        && acc
    , new Array(rowsCount).fill(0).map(a=> []))
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */
