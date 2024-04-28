# https://leetcode.com/problems/factorial-generator/description/

/**
 * @param {number} n
 * @yields {number}
 */
function* factorial(n) {

    if (n === 0) {
    yield 1;
  }
  else {
    let seq = 1;
    for (let i = 1; i <= n; i++) {
      seq *= i;
      yield seq;
    }
  }
    
};

/**
 * const gen = factorial(2);
 * gen.next().value; // 1
 * gen.next().value; // 2
 */
