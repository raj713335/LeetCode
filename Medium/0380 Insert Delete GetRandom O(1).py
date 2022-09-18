# https://leetcode.com/problems/insert-delete-getrandom-o1/


import random

class RandomizedSet:

    def __init__(self):
        self.random = {}
        

    def insert(self, val: int) -> bool:
        
        
        if val in self.random:
            return False
        else:
            self.random[val] = 1
            return True
        

    def remove(self, val: int) -> bool:
        
        if val in self.random:
            self.random.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        rendx = random.randint(0,len(self.random)-1)
        return list(self.random.keys())[rendx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
