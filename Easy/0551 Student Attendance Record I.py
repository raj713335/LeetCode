# https://leetcode.com/problems/student-attendance-record-i/


class Solution:
    def checkRecord(self, s: str) -> bool:
        
        if s.count("A") >= 2:
            return False
        
        max_count = 0
        count = 0 



        for each in s:
            if each == "L":
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0

        if max_count >= 3:
            return False
        else:
            return True
            
            
        
