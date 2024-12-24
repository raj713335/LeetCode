# https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        while list1 and list2:

            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next

            curr.next = ListNode(val)
            curr = curr.next

        while list2 == None and list1 != None:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next
        
        while list1 == None and list2 != None:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next

        return dummy.next
