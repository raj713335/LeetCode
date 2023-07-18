# https://leetcode.com/problems/lru-cache/description/


class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        self.recent = []

    def get(self, key: int) -> int:

        if key in self.lru:
            self.recent.remove(key)
            self.recent.append(key)
            return self.lru[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.lru:
            self.recent.remove(key)
            self.recent.append(key)
            self.lru[key] = value
        elif len(self.lru.keys()) < self.capacity:
            self.recent.append(key)
            self.lru[key] = value
        else:
            rmkey = self.recent[0]
            del self.recent[0]
            self.recent.append(key)
            del self.lru[rmkey]
            self.lru[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
