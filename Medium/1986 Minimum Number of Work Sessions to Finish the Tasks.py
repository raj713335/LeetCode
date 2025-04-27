# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:

        n = len(tasks)
        
        # Sort tasks in decreasing order to prioritize larger tasks first
        tasks.sort(reverse=True)

        # Memoization table to store results for different task states
        memo = {}

        def backtrack(index, sessions):
            # If all tasks are assigned, return the number of sessions used
            if index == n:
                return len(sessions)

            # Memoization key: (index, tuple of session states)
            state = tuple(sessions)
            if (index, state) in memo:
                return memo[(index, state)]

            # Try to add the current task to each session
            min_sessions = float('inf')
            for i in range(len(sessions)):
                if sessions[i] + tasks[index] <= sessionTime:
                    sessions[i] += tasks[index]
                    min_sessions = min(min_sessions, backtrack(index + 1, sessions))
                    sessions[i] -= tasks[index]

            # If task doesn't fit in any current session, start a new session
            sessions.append(tasks[index])
            min_sessions = min(min_sessions, backtrack(index + 1, sessions))
            sessions.pop()

            memo[(index, state)] = min_sessions
            return min_sessions

        # Start the backtracking process with no tasks assigned
        return backtrack(0, [])
        
