# https://leetcode.com/problems/generate-circular-array-values/description/


/**
 * @param {Array<number>} arr
 * @param {number} startIndex
 * @yields {number}
 */
var cycleGenerator = function* (arr, startIndex) {

    let curIdx = startIndex
    let jump
    
    
    while(true) {
        jump = yield arr[curIdx]
        curIdx += jump
        curIdx = curIdx % arr.length
        if(curIdx < 0) curIdx += arr.length
    }
    
};

/**
 *  const gen = cycleGenerator([1,2,3,4,5], 0);
 *  gen.next().value  // 1
 *  gen.next(1).value // 2
 *  gen.next(2).value // 4
 *  gen.next(6).value // 5
 */
