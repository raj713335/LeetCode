# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        

        l, r = 0, len(letters) - 1

        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        while l <= r:
            mid = (l+r)//2

            if letters[mid] <= target:
                l = mid + 1
            elif letters[mid] > target:
                r = mid - 1


        return letters[l]
        
        
