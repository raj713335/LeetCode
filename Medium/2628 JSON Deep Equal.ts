# https://leetcode.com/problems/json-deep-equal/description/

function areDeeplyEqual(o1: any, o2: any): boolean {

    const typeO1 = typeof o1;
    const typeO2 = typeof o2;
    if(typeO1 !== typeO2) return false;
    if(Array.isArray(o1) !== Array.isArray(o2)) return false;
    if(o1===null || o2===null || typeO1 !== 'object' || typeO2 !== 'object') return o1===o2;
    
    const o1Keys = Object.keys(o1);
    const o2Keys = Object.keys(o2);
    if(o1Keys.length !== o2Keys.length) return false;
    for(const key of o1Keys) {
        if(!o2Keys.includes(key)) return false;
        if(!areDeeplyEqual(o1[key], o2[key])) return false;
    }

    return true;

};
