# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        
        group = -1

        while head:
            stack = []
            balance = group + 1
            length = 0

            while head and balance > 0:
                
                stack.append(head.val)
                head = head.next
                length += 1
                balance -= 1
                
            if len(stack) % 2 == 0:
                for each in stack[::-1]:
                    curr.next = ListNode(each)
                    curr = curr.next
            else:
                for each in stack:
                    curr.next = ListNode(each)
                    curr = curr.next

            group += 1

        return dummy.next
