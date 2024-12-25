# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        dictx = {}

        while head:
            val = head.val
            if val not in dictx:
                dictx[val] = 1
            else:
                dictx[val] += 1

            head = head.next

        for each in dictx.keys():
            if dictx[each] == 1:
                curr.next = ListNode(each)
                curr = curr.next

        return dummy.next
