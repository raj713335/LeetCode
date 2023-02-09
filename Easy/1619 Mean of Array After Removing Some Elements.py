# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

class Solution:
    def trimMean(self, arr: List[int]) -> float:

        arr = sorted(arr)

        length = len(arr)//10

        return sum(arr[length//2:-length//2])/(len(arr)-length)
