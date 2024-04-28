# https://leetcode.com/problems/inversion-of-object/description/

/**
 * @param {Object} obj
 * @return {Object}
 */
var invertObject = function(obj) {
  const invertedObj = {};
  
  for (const key in obj) {
    const value = obj[key];
    
    if (invertedObj[value] === undefined) {
      invertedObj[value] = key;
    } else {
      if (Array.isArray(invertedObj[value])) {
        invertedObj[value].push(key);
      } else {
        invertedObj[value] = [invertedObj[value], key];
      }
    }
  }
  
  return invertedObj;
}
