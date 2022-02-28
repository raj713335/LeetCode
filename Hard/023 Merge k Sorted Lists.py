# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        heapq.heapify(res)

        for head in lists :
            temp=head
            while temp is not None :
                heapq.heappush(res,temp.val)
                temp=temp.next

        prev=None
        new_head=None
        while res :
            curr=heapq.heappop(res)
            node=ListNode(curr)

            if prev:
                prev.next=node
            else:
                new_head=node
            prev=node

        return new_head
