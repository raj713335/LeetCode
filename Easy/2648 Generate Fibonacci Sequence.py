# https://leetcode.com/problems/generate-fibonacci-sequence/description/


function* fibGenerator(): Generator<number, any, number> {

    yield 0;

    yield 1;
    
    let a: number = 0;
    let b: number = 1;
    
    while (true) {
        const c: number = a + b;
        a = b;
        b = c;
        yield c;
    }

};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
