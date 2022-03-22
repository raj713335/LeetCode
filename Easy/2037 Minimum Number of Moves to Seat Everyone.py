# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        
        count = 0 
        
        for i in range(0, len(students)):
            count += abs(students[i]-seats[i])
            
        return count
            
        
