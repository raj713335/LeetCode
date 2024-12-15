# https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150

class MinStack:

    def __init__(self):
        self.value = []
        

    def push(self, val: int) -> None:
        self.value.append(val)
        

    def pop(self) -> None:
        self.value.pop()
        

    def top(self) -> int:
        top = self.value[-1]
        return top
        

    def getMin(self) -> int:
        return min(self.value)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
