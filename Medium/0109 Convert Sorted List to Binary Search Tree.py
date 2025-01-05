# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        def construct_bst(values):
            if not values:
                return 

            mid = len(values) // 2
            node = TreeNode(values[mid])

            node.left = construct_bst(values[:mid])
            node.right = construct_bst(values[mid+1:])

            return node

        return construct_bst(stack)
        
