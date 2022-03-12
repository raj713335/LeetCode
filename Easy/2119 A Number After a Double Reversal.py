# https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        if len(str(num)) == 1:
            return True
        reversed1 = list(str(num)[::-1])
        count = 0
        for i in range(0, len(reversed1)):
            if reversed1[i] == "0":
                count +=1
            else:
                break
        reversed2 = reversed1[count:][::-1]
        count = 0
        for i in range(0, len(reversed2)):
            if reversed2[i] == "0":
                count += 1
            else:
                break

        reversed2 = reversed2[count:]

        if str(num) == "".join(reversed2):
            return True
        else:
            return False
