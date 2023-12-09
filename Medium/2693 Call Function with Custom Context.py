# https://leetcode.com/problems/call-function-with-custom-context/description/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };

declare global { 
    interface Function {
      callPolyfill(context: Record<string, JSONValue>, ...args: JSONValue[]): JSONValue;
	}
}

Function.prototype.callPolyfill = function(context, ...args): JSONValue {
    return this.apply(context, args)
	
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */
