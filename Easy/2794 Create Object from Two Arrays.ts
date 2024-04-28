# https://leetcode.com/problems/create-object-from-two-arrays/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

function createObject(keysArr: JSONValue[], valuesArr: JSONValue[]): Record<string, JSONValue> {

    const set = new Set<string>();
    const obj = {}
    keysArr.forEach((key, index) => {
        if (!set.has(String(key))) {
            obj[String(key)] = valuesArr[index];
            set.add(String(key))
        }
    })
    return obj
    
};
