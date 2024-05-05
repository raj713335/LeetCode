# https://leetcode.com/problems/immutability-helper/description/

type InputObj = Record<any, any> | Array<any>;
type Mutations = Map<string | symbol | number, unknown>;
type Nested = Map<string | symbol | number, any>;
type DraftState = [Nested, Mutations, InputObj];

class ImmutableHelper {
  constructor(private readonly obj: InputObj) {}

  public produce(mutator: (obj: any) => void): any {
    const draft = this.createDraft(this.obj);
    mutator(draft);

    return this.assemble(draft);
  }

  private draftStates = new WeakMap<object, DraftState>();

  private createDraft = (obj: any): InputObj => {
    // Mutated values
    const mutations: Mutations = new Map();
    // Nested drafts for nested objects
    const nested = new Map<string | symbol | number, any>();
    const draft = new Proxy(obj, {
      set: (_, p, v) => {
        mutations.set(p, v);
        if (mutations.get(p) === obj[p]) {
          // remove useless mutation
          mutations.delete(p);
        }

        return true;
      },
      get: (_, p) => {
        if (typeof obj[p] === 'object' && obj[p]) {
          if (!nested.has(p)) {
            nested.set(p, this.createDraft(obj[p]));
          }
          return nested.get(p)!;
        }
        if (mutations.has(p)) {
          return mutations.get(p);
        }

        return obj[p];
      },
    });
    this.draftStates.set(draft, [nested, mutations, obj]);

    return draft;
  };

  // assembles object from initial one, mutations and nested drafts
  private assemble = (proxy: any) => {
    const isProxy = this.draftStates.has(proxy);
    if (!isProxy) {
      return proxy;
    }

    const [nested, mutations, original] = this.draftStates.get(proxy)!;
    // No modifications, return initial object
    if (!mutations.size && !nested.size) {
      return original;
    }

    const next: any = Array.isArray(original)
      ? [...original]
      : Object.assign({}, original);
    // assemble every nested draft
    nested.forEach((v, k) => {
      next[k] = this.assemble(v);
    });
    // set mutated keys
    mutations.forEach((v, k) => {
      next[k] = v;
    });

    return next;
  };
}

/**
 * const originalObj = {"x": 5};
 * const mutator = new ImmutableHelper(originalObj);
 * const newObj = mutator.produce((proxy) => {
 *   proxy.x = proxy.x + 1;
 * });
 * console.log(originalObj); // {"x: 5"}
 * console.log(newObj); // {"x": 6}
 */
