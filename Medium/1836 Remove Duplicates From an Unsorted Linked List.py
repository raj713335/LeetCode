# https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        dictx = {}

        curr = head

        while curr:
            val = curr.val
            if val not in dictx:
                dictx[val] = 1
            else:
                dictx[val] += 1
            curr = curr.next

        dummy = ListNode(0,head)
        slow = dummy
        curr = head

        while curr:
            if dictx[curr.val] == 1:
                slow.next = curr
                slow = slow.next
            curr = curr.next

        slow.next = None    
        return dummy.next  
        
