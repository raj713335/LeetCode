# https://leetcode.com/problems/linked-list-components/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        dictx = {}

        for each in nums:
            dictx[each] = 1

        flag = False
        count = 0

        while head:
            if head.val in dictx:
                if not flag:
                    flag = True
                    count +=1 
            else:
                flag = False

            head = head.next

        return count
