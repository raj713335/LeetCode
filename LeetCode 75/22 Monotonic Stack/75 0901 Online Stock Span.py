# https://leetcode.com/problems/online-stock-span/description/

class StockSpanner:

    def __init__(self):
        self.a = []
        

    def next(self, price: int) -> int:

        count = 1
        if not self.a:
            self.a.append((price, count))
        else:
            i = len(self.a)-1
            while i>=0 and self.a[i][0]<=price:
                count += self.a[i][1]
                i -= self.a[i][1]
            self.a.append((price,count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
