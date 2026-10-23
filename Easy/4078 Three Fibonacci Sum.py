# https://leetcode.com/problems/three-fibonacci-sum/description/

class Solution:
    def threeFibonacciSum(self, n: int) -> bool:

        listx = [0, 1]

        while listx[-1] <= n:
            a, b = listx[-2], listx[-1] 
            c = a + b

            if a + b + c == n:
                return True

            listx.append(c)
        
        return False
        
