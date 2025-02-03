# https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = 0

        for num in digits:
            res = res * 10 + num

        res = res + 1

        res_arr = []

        for num in str(res):
            res_arr.append(int(num))

        return res_arr
        
        
        # output = ""
        # for each in digits:
        #     output += str(each)
            
        # output = int(output)+1
        
        # return list(map(int, str(output)))
        
