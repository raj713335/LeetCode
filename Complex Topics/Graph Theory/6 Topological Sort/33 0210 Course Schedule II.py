# https://leetcode.com/problems/course-schedule-ii/description/


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Code here
        
        adjancy_matrix = defaultdict(list)
        
        for u, v in prerequisites:
            adjancy_matrix[u].append(v)
        
        indegree = defaultdict(int)
        
        
        for u, v in prerequisites:
            indegree[v] += 1
            
        q = deque()
        
        
        for i in range(0, numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        topo_order = []       
        
        while q:
            
            node = q.popleft()
            topo_order.append(node)
            
            for next in adjancy_matrix[node]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)
        
        # If topo_order contains all nodes, return it
        if len(topo_order) == numCourses:
            return topo_order[::-1]
        else:
            return []  # Cycle exists (not possible in DAG by definition)



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output
        

        
