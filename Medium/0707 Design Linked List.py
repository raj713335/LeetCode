# https://leetcode.com/problems/design-linked-list/description/

class MyLinkedList:

    def __init__(self):
        self.list = []
        

    def get(self, index: int) -> int:
        try:
            return self.list[index]
        except:
            pass

        return -1
        

    def addAtHead(self, val: int) -> None:
        self.list.insert(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.list.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if len(self.list) >= index:
            self.list.insert(index, val)
        

    def deleteAtIndex(self, index: int) -> None:
        try:
            del self.list[index]
        except:
            pass
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
