# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        A, B = list1, list2
        for _ in range(a-1):
            A =  A.next
            
        remainA = A.next
        for _ in range(b-a+1):
            remainA = remainA.next
            
        A.next = B
        while B.next:
            B = B.next
        
        B.next = remainA
        return list1

            
                
            
        
