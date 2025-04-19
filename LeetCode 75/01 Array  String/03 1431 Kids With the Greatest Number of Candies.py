# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        res = []
        
        max_candy = max(candies)
        
        for i in range(0, len(candies)):
            if candies[i]+extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)
                
        return res
        
