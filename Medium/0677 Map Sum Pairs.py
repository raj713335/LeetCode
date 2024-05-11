# https://leetcode.com/problems/map-sum-pairs/description/


class MapSum:

    def __init__(self):
        self.dictx = {}   

    def insert(self, key: str, val: int) -> None:
        self.dictx[key] = val
        
    def sum(self, prefix: str) -> int:
        sumx = 0
        length = len(prefix)

        for key, val in self.dictx.items():
            if key[:length] == prefix:
                sumx += val

        return sumx

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
