# https://leetcode.com/problems/make-object-immutable/description/


/**
 * @param {Object|Array} obj
 * @return {Object|Array} immutable obj
 */
var makeImmutable = function(obj) {

    return new Proxy(obj, {
        set(target, prop, value, receiver){
            if (Array.isArray(target) && typeof prop === 'string'){
                const asNumber = Number(prop);
                if (asNumber !== undefined){
                    throw `Error Modifying Index: ${prop}`;
                }
            }            
            throw `Error Modifying: ${prop}`;
        },
        get(target, prop){
            if (Array.isArray(target) && (
                prop==='pop' || prop==='push' || prop==='shift' || prop==='unshift' ||
                prop==='splice' || prop==='sort' || prop==='reverse'
            )){
                return (...arguments) => {throw `Error Calling Method: ${prop}`};
            }
            if (typeof obj[prop] === 'object' && obj[prop] !== null){
                // call recursively
                return makeImmutable(obj[prop]);
            }
            return Reflect.get(target, prop); // execute default behavior
        }
    });
    
};

/**
 * const obj = makeImmutable({x: 5});
 * obj.x = 6; // throws "Error Modifying x"
 */
