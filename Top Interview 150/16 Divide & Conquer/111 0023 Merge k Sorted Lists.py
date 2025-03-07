# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # If lists is empty, return None
            return None
        return self.mergeDivide(lists, 0, len(lists) - 1)

    def mergeDivide(self, lists, left, right):
        if left == right:  # Base case: only one list to return
            return lists[left]

        mid = (left + right) // 2
        left_merged = self.mergeDivide(lists, left, mid)
        right_merged = self.mergeDivide(lists, mid + 1, right)

        return self.mergeTwoLists(left_merged, right_merged)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # Append remaining nodes
        curr.next = l1 if l1 else l2

        return dummy.next
