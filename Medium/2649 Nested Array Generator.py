# https://leetcode.com/problems/nested-array-generator/description/

type MultidimensionalArray = (MultidimensionalArray | number)[]

function* inorderTraversal(arr: MultidimensionalArray): Generator<number, void, unknown> {
    // @ts-ignore
    const flattenArray = arr.flat(Infinity);

    for (let item of flattenArray) yield item;
	
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
