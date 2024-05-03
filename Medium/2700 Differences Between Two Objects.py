# https://leetcode.com/problems/differences-between-two-objects/


type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>

function objDiff(obj1: any, obj2: any): any {

    // support variables
    let t1 = Array.isArray(obj1) ? 'array' : typeof obj1,
        t2 = Array.isArray(obj2) ? 'array' : typeof obj2;
    // base case - different types
    if (t1 !== t2) return [obj1, obj2];
    // both are objects
    if (t1 === 'object' || t1 === 'array') return Object.fromEntries(
        Object.entries(obj1).reduce((acc, [key, el1]) => {
            const el2 = obj2[key];
            // el2 does not exist or el1 === el2
            if (el2 === undefined || el1 === el2) return acc;
            // el1 and el2 are different
            const tmp = objDiff(el1, el2);
            // skipping keys with no diffs
            if (!Object.keys(tmp).length) return acc;
            acc.push([key, tmp]);
            return acc;
        }, [])
    );
    return [obj1, obj2];
    
};
