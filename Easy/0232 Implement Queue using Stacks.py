# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue) > 0:
            x = self.queue[0]
            del self.queue[0]
            return x
             
        

    def peek(self) -> int:
        if len(self.queue) > 0:
            x = self.queue[0]
            return x
        

    def empty(self) -> bool:
        if len(self.queue) > 0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
