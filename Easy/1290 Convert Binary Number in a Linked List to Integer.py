# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        number = ""
        output = 0
        current = head
        while (current != None):
            number += str(current.val)
            current = current.next
        
        number = number[::-1]
        
        for i in range(0, len(number)):
            output += int(number[i]) * (2**i)
        
        return output
        
