# https://leetcode.com/problems/is-object-empty/description/

function isEmpty(obj: Record<string, any> | any[]): boolean {
      for (let value in obj) {
      return false;
    }

    return true;

};
