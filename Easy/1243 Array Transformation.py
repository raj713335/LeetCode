# https://leetcode.com/problems/array-transformation/description/


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        arr_new = arr[:]
        flag = True

        while flag:
            flag = False
            for i in range(1, len(arr)-1):
            
                if  arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    arr_new[i] = arr[i] - 1
                    flag = True

                elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    arr_new[i] = arr[i] + 1
                    flag = True
                else:
                    arr_new[i] = arr[i]
            arr = arr_new[:]

        return arr
        
