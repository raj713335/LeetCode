# https://leetcode.com/problems/sort-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves
        def find_middle(head):
            slow, fast = head, head.next  # Fast starts at second node to split correctly
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow  # Middle node (end of first half)

        mid = find_middle(head)
        right_head = mid.next
        mid.next = None  # Split the list into two halves

        # Step 2: Sort each half recursively
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_head)

        # Step 3: Merge two sorted halves
        def merge(l1, l2):
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
        
            curr.next = l1 if l1 else l2
            
            return dummy.next

        return merge(left_sorted, right_sorted)
        
