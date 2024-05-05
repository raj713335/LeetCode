# https://leetcode.com/problems/convert-json-string-to-object/description/


/**
 * @param {string} str
 * @return {null|boolean|number|string|Array|Object}
 */
var jsonParse = function(str) {

    return eval(`() => (${str})`)();
    
};
