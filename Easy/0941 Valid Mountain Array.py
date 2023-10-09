# https://leetcode.com/problems/valid-mountain-array/description/


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        flag = False
        count = 0

        cx1 = False
        cx2 = False

        if len(arr) < 3:
            return False

        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                cx1 = True
                if flag:
                    count += 1
            elif arr[i-1] > arr[i]:
                flag = True
                cx2 = True
            else:
                return False


        if count == 0 and cx1 and cx2:
            return True
        return False
        
