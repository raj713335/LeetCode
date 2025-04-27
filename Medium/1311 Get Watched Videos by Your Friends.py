# https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

from collections import deque, Counter

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        n = len(watchedVideos)
        visited = [False] * n
        queue = deque()
        
        queue.append(id)
        visited[id] = True
        current_level = 0

        while queue and current_level < level:
            for _ in range(len(queue)):
                person = queue.popleft()
                for friend in friends[person]:
                    if not visited[friend]:
                        visited[friend] = True
                        queue.append(friend)
            current_level += 1

        # Now, queue contains all friends at the target level
        counter = Counter()
        for person in queue:
            for video in watchedVideos[person]:
                counter[video] += 1

        # Sort by frequency first, then by name
        result = sorted(counter.items(), key=lambda x: (x[1], x[0]))

        # Extract only video names
        return [video for video, freq in result]
        
