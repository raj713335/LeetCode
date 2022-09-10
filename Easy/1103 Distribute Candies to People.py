# https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        output = [0] * num_people
        n = 0
        i = 1
        
        while candies > 0:
            
            if n == num_people:
                n = 0
                
            output[n] += i
            candies -= i
            i += 1
            n += 1
            
        output[n-1] += candies
        
        return output
            
        
