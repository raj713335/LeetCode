# https://leetcode.com/problems/rotated-digits/description/


class Solution:
    def rotatedDigits(self, n: int) -> int:

        count = 0
        main_roatr = {"2":0, "5":0, "6":0, "9":0}
        temp_roatr = {"3": 0, "4": 0, "7": 0}

        for i in range(1, n+1):
            temp_count = 0
            flag = True
            for each in list(str(i)):
                if each in main_roatr:
                    temp_count = 1
                elif each in temp_roatr:
                    flag = False
            if flag:
                count += temp_count

        return count

        
        
