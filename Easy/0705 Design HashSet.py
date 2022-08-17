# https://leetcode.com/problems/design-hashset/


class MyHashSet:

    def __init__(self):
        self.dictx = {}
        

    def add(self, key: int) -> None:
        self.dictx[key] = 1
        

    def remove(self, key: int) -> None:
        if key in self.dictx:
            del self.dictx[key]
        

    def contains(self, key: int) -> bool:
        if key in self.dictx:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
