# https://leetcode.com/problems/keys-and-rooms/description/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        len_rooms = len(rooms)

        grid = [False] * len_rooms
        grid[0] = True
        visited = set()

        def dfs(room_keys):

            if room_keys in visited:
                return
            
            grid[room_keys] = True
            visited.add(room_keys)

            for keys in rooms[room_keys]:
                if keys not in visited:
                    dfs(keys)
            

        dfs(0)

        for each in grid:
            if each == False:
                return False
                
        return True

        

        