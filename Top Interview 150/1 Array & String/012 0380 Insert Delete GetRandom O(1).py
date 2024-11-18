# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

import random

class RandomizedSet:

    def __init__(self):
        self.random = {}
        

    def insert(self, val: int) -> bool:

        if val not in self.random:
            self.random[val] = 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:

        if val in self.random:
            del self.random[val]
            return True
        else:
            return False

    def getRandom(self) -> int:

        rand_index = random.randint(0, len(self.random)-1)
        return list(self.random.keys())[rand_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
