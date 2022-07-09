# https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        record = []
        
        for each in ops:
            print(record)
            if each == "C":
                record.pop()
            elif each == "D":
                record.append(int(record[-1])*2)
            elif each == "+":
                record.append(int(record[-1])+int(record[-2]))
            else:
                record.append(int(each))
                
        return sum(record)
        
        
