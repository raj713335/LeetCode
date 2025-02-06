# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        manager_to_subordinates = defaultdict(list)
        for employee, manager_id in enumerate(manager):
            if employee != headID:
                manager_to_subordinates[manager_id].append(employee)

        
        queue = deque([(headID, 0)])
        max_time = 0

        while queue:
            current_head, current_time = queue.popleft()

            max_time = max(max_time, current_time) 

            for child in manager_to_subordinates[current_head]:
                queue.append((child, current_time + informTime[current_head]))

        return max_time
