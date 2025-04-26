# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions = sorted(potions)
        res = []

        for spell in spells:

            l, r = 0, len(potions)-1
            index = len(potions)

            while (l <= r):
                mid = (l+r)//2

                if potions[mid] * spell >= success:
                    r = mid-1
                    index = mid
                else:
                    l = mid+1

            res.append(len(potions)-index)

        return res
                    

            

