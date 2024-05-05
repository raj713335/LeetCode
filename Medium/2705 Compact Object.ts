# https://leetcode.com/problems/compact-object/description/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {

    if (Array.isArray(obj)) {
    return obj.filter(Boolean).map(val => {
        if (typeof val === 'object') {
          return compactObject(val);
        }
        return val;
      })
     
    }

    for (const [key,val] of Object.entries(obj)) {

        if (!val) {
            delete obj[key];
            continue;
        }
        
        if (typeof val === 'object') {
            obj[key] = compactObject(val);
        }
    }

    return obj;
    
};
