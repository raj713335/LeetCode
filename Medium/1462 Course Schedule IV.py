# https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        preMap = { i : [] for i in range(numCourses)}

        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        prereqmap = {}
        res = []

        def dfs(crs):
            if crs not in prereqmap:
                prereqmap[crs] = set()
                for preq in preMap[crs]:
                    prereqmap[crs] |=  dfs(preq)
                prereqmap[crs].add(crs)
            return prereqmap[crs]

        for crs in range(numCourses):
            dfs(crs)


        for crs, preq in queries:
            res.append(preq in prereqmap[crs])

        return res
        
        
