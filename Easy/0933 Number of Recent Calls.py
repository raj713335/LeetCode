# https://leetcode.com/problems/number-of-recent-calls/description/

class RecentCounter:

    def __init__(self):
        self.s = []
        

    def ping(self, t: int) -> int:
        
        while self.s and t - self.s[0] > 3000:
            self.s.pop(0)  # remove 1st el if it's 3000+ away from t
        self.s.append(t)
        return len(self.s) 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
