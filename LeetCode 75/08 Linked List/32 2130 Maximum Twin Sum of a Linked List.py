# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        arr = []
        n = 0
        
        current = head
        
        while current != None:
            
            arr.append(current.val)
            current = current.next
            n += 1
            
        best = 0
        
        for i in range(n):
            best = max(best, arr[i]+arr[n-i-1])
            
        return best
