# https://leetcode.com/problems/design-task-manager/description/


import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskMap = {}  # taskId -> (priority, userId)
        self.heap = []     # max-heap: (-priority, -taskId, userId)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (priority, userId)
        heapq.heappush(self.heap, (-priority, -taskId, userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.taskMap:
            _, userId = self.taskMap[taskId]
            self.taskMap[taskId] = (newPriority, userId)
            heapq.heappush(self.heap, (-newPriority, -taskId, userId))
        

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskMap:
            del self.taskMap[taskId]
            # No need to remove from heap; lazy deletion handles it

        

    def execTop(self) -> int:
        while self.heap:
            negPriority, negTaskId, userId = heapq.heappop(self.heap)
            taskId = -negTaskId
            priority = -negPriority
            if taskId in self.taskMap:
                # Validate priority hasn't changed since push
                curPriority, curUserId = self.taskMap[taskId]
                if curPriority == priority and curUserId == userId:
                    # Valid task
                    del self.taskMap[taskId]
                    return userId
                # Else: stale entry, skip
        return -1  # No tasks left
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
