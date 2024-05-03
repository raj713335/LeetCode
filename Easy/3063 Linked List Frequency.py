# https://leetcode.com/problems/linked-list-frequency/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Dictionary to store the frequency of each element
        frequency_map = collections.defaultdict(int)

        # Traverse the original linked list and count the frequency of each element
        current_node = head

        while current_node:
            frequency_map[current_node.val] += 1
            current_node = current_node.next

        # Create a new linked list to store the frequencies
        dummy = ListNode()
        new_linked_list = dummy
        # Iterate through the frequency map and add each frequency to the new linked list
        for val, freq in frequency_map.items():
            new_linked_list.next = ListNode(freq)
            new_linked_list = new_linked_list.next

        # Return the head of the new linked list
        return dummy.next
