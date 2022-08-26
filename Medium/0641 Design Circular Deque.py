# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.dqueue = []
        

    def insertFront(self, value: int) -> bool:
        if len(self.dqueue) < self.k:
            self.dqueue.insert(0, value)
            return True
        else:
            return False
            
        

    def insertLast(self, value: int) -> bool:
        if len(self.dqueue) < self.k:
            self.dqueue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.dqueue) > 0:
            del self.dqueue[0]
            return True
        else:
            return False
        

    def deleteLast(self) -> bool:
        if len(self.dqueue) > 0:
            del self.dqueue[-1]
            return True
        else:
            return False
        

    def getFront(self) -> int:
        if len(self.dqueue) > 0:
            return self.dqueue[0]
        else:
            return -1
        

    def getRear(self) -> int:
        if len(self.dqueue) > 0:
            return self.dqueue[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.dqueue) == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        if len(self.dqueue) == self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
