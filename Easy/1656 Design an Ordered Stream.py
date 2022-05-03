# https://leetcode.com/problems/design-an-ordered-stream/


class OrderedStream:

    def __init__(self, n: int):
        self.dd = {i: "" for i in range(1, n+1)}
        self.next_val = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dd[idKey] = value
        if idKey == self.next_val:
            try:
                self.next_val = next(i for i in self.dd.keys() if i >= idKey and len(self.dd[i])==0)
            except: 
                self.next_val = len(self.dd) + 1
            return [self.dd[ii] for ii in range(idKey, self.next_val)]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
