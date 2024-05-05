# https://leetcode.com/problems/query-batching/description/

/**
 * @param {Function} queryMultiple
 * @param {number} t
 * @return {void}
 */
var QueryBatcher = function(queryMultiple, t) {

    this.t = t;
    this.qmt = 0;
    this.queries = [];

    this.queryMultiple = (...args) => {
        this.qmt = Date.now()
        return queryMultiple(...args);
    };
    
};

/**
 * @param {string} key
 * @return {Promise<string>}
 */
QueryBatcher.prototype.getValue = async function(key) {

    const elapsed = Date.now() - this.qmt
    if (elapsed > this.t) {
        return (await this.queryMultiple([key]))[0]
    }

    return new Promise(resolve => {
        if (this.queries.push({ key, resolve }) === 1) {
            setTimeout(async () => {
                const queries = this.queries
                this.queries = []
                const values = await this.queryMultiple(queries.map(query => query.key))
                queries.forEach(({ resolve }, i) => resolve(values[i]))
            }, this.t - elapsed)
        }
    });
    
};

/**
 * async function queryMultiple(keys) { 
 *   return keys.map(key => key + '!');
 * }
 *
 * const batcher = new QueryBatcher(queryMultiple, 100);
 * batcher.getValue('a').then(console.log); // resolves "a!" at t=0ms 
 * batcher.getValue('b').then(console.log); // resolves "b!" at t=100ms 
 * batcher.getValue('c').then(console.log); // resolves "c!" at t=100ms 
 */
