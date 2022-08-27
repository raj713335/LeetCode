# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.value = []
        self.k = k
        

    def enQueue(self, value: int) -> bool:
        if len(self.value) < self.k:
            self.value.append(value)
            #print(self.value)
            return True
        else:
            return False
        
        
        

    def deQueue(self) -> bool:
        if len(self.value) != 0:
            del self.value[0]
            return True
        else:
            return False
        

    def Front(self) -> int:
        if len(self.value) != 0:
            return self.value[0]
        else:
            return -1
        

    def Rear(self) -> int:
        if len(self.value) != 0:
            return self.value[-1]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if len(self.value) == 0:
            return True
        else:
            return False
        
        

    def isFull(self) -> bool:
        if len(self.value) == self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
