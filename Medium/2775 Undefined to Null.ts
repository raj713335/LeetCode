# https://leetcode.com/problems/undefined-to-null/description/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Value = undefined | null | boolean | number | string | Value[] | { [key: string]: Value };

type Obj1 = Record<string, Value> | Array<Value>
type Obj2 = Record<string, JSONValue> | Array<JSONValue>

function undefinedToNull(obj: Obj1): Obj2 {

    if (obj == null) {
        return null;
    }

    if (Array.isArray(obj)) {
        return obj.map(item => undefinedToNull(item as any));
    }

    if (typeof obj === "object") {
        const newObj = {};
        for (const key in obj) {
            newObj[key] = undefinedToNull(obj[key] as any);
        }

        return newObj;
    }

    return obj;
    
};

/**
 * undefinedToNull({"a": undefined, "b": 3}) // {"a": null, "b": 3}
 * undefinedToNull([undefined, undefined]) // [null, null] 
 */
