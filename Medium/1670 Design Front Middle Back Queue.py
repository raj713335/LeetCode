# https://leetcode.com/problems/design-front-middle-back-queue/description/


class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque()
        print("FrontMiddleBackQueue", self.queue)
        

    def pushFront(self, val: int) -> None:
        self.queue.appendleft(val)
        print("pushFront", self.queue)
        

    def pushMiddle(self, val: int) -> None:
        length = len(self.queue)
        if length % 2 == 0:
            index = (length//2)
        else:
            index = (length//2)
        self.queue.insert(index, val)
        print("pushMiddle", self.queue)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        print("pushBack", self.queue)
        

    def popFront(self) -> int:
        if self.queue:
            return self.queue.popleft()
        return -1
        

    def popMiddle(self) -> int:
        if self.queue:
            length = len(self.queue)
            if length % 2 == 0:
                index = (length//2) -1 
            else:
                index = (length//2)
            val = self.queue[index]
            del self.queue[index]
            return val
        return -1

    def popBack(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
