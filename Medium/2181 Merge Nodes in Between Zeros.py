# https://leetcode.com/problems/merge-nodes-in-between-zeros/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        val = ListNode()
        output = val
        sumx = -1
        
        while (current != None):
            
            temp = current.val 
            current = current.next
            
            if temp == 0:
                if sumx == -1:
                    sumx = 0
                else:
                    output.next = ListNode(sumx)
                    output = output.next
                    sumx = 0
            else:
                sumx += temp
      
        return val.next
            
        
