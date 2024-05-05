# https://leetcode.com/problems/check-if-object-instance-of-class/description/


function checkIfInstanceOf(obj: any, classFunction: any): boolean {

    if (obj == null || typeof classFunction !== 'function' ) return false;
    return Object(obj) instanceof classFunction;
    
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
