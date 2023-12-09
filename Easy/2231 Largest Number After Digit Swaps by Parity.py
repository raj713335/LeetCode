# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/


class Solution:
    def largestInteger(self, num: int) -> int:

        temp_number = list(str(num))

        even = []
        odd = []

        for i in range(0, len(temp_number)):
            if int(temp_number[i]) % 2 == 0:
                even.append(temp_number[i])
            else:
                odd.append(temp_number[i])

        even = sorted(even, reverse = True)
        odd = sorted(odd, reverse = True)


        eIndex = 0
        oIndex = 0
        
        for i in range(len(temp_number)):
            if int(temp_number[i]) % 2 == 0:
                temp_number[i]  = even[eIndex]
                eIndex = eIndex + 1
            else:
                temp_number[i] = odd[oIndex]
                oIndex = oIndex + 1
   
        return int("".join(temp_number))
        
