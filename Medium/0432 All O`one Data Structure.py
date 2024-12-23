# https://leetcode.com/problems/all-oone-data-structure/description/

import math

class AllOne:

    def __init__(self):
        self.dictx = {}
        

    def inc(self, key: str) -> None:
        if key not in self.dictx:
            self.dictx[key] = 1
        else:
            self.dictx[key] += 1
        

    def dec(self, key: str) -> None:
        if key in self.dictx:
            self.dictx[key] -= 1
            if self.dictx[key] == 0:
                del self.dictx[key]
        

    def getMaxKey(self) -> str:

        max_key, valux = "", 0

        for key,val in self.dictx.items():
            if val > valux:
                valux = val
                max_key = key

        return max_key

        

    def getMinKey(self) -> str:

        min_key, valux = "", math.inf

        for key,val in self.dictx.items():
            if val < valux:
                valux = val
                min_key = key

        return min_key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
