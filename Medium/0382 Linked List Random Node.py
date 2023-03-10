# https://leetcode.com/problems/linked-list-random-node/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
class Solution:

    def __init__(self, head: Optional[ListNode]):

        self.head = head
        self.count = 0
        
        root = self.head

        while root:

            root = root.next
            self.count += 1

        
        

    def getRandom(self) -> int:

        root = self.head

        itr = random.randint(1, self.count)
        val = 0
        while root and itr > 0:
            val = root.val
            root = root.next
            itr -= 1

        return val


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
