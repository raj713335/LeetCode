# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

sys.set_int_max_str_digits(100000)

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode()
        curr = dummy
        nummber = ""

        while head:
            nummber += str(head.val)
            head = head.next

        nummber = list(str(int(nummber) * 2))

        for each in nummber:
            curr.next = ListNode(int(each))
            curr = curr.next

        return dummy.next
        
