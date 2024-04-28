# https://leetcode.com/problems/infinite-method-object/description/

function createInfiniteObject(): Record<string, () => string> {

    return new Proxy({}, {
        get: (_, key) => {
            return () => String(key);
        }
    });
    
};

/**
 * const obj = createInfiniteObject();
 * obj['abc123'](); // "abc123"
 */
