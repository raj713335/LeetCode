# https://leetcode.com/problems/design-most-recently-used-queue/description/

class MRUQueue:

    def __init__(self, n: int):

        self.n = [x for x in range(1, n+1)]

        
    def fetch(self, k: int) -> int:

        val = self.n[k-1]
        del self.n[k-1]
        self.n.append(val)
        return val
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
