https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/submissions/

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ans = []
        
        for query in queries:
            count = 0
            for point in points:
                dist = sqrt(pow((query[0]-point[0]),2)+ pow((query[1]-point[1]),2))
                if dist <= query[2]:
                    count += 1
            ans.append(count)
        return ans
        
        
