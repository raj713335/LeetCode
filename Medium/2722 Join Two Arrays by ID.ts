# https://leetcode.com/problems/join-two-arrays-by-id/description/


type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {

    let  mapResult = new Map<number, ArrayType>();

   for( const element of arr1 ){
        mapResult.set(element.id, element);
    }

    for (const element2 of arr2) {
            const merger = mapResult.has(element2.id) 
                ? { ...mapResult.get(element2.id), ...element2 }
                : element2;

            mapResult.set(element2.id, merger)
    }

    return [...mapResult.values()].sort((a, b) => a.id - b.id);
    
};
