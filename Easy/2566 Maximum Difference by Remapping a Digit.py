# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num: int) -> int:

        num1 = list(str(num))

        flag = True
        key = ""

        for i in range(0, len(num1)):
            if flag:
                if num1[i] != "9":
                    if key == "":
                        key = num1[i]
                        num1[i] = "9"
                        flag = False
            else:
                if num1[i] == key:
                    num1[i] = "9"
        

        num2 = list(str(num))

        flag = True
        key = ""

        for i in range(0, len(num2)):
            if flag:
                if num2[i] != "0":
                    if key == "":
                        key = num2[i]
                        num2[i] = "0"
                        flag = False
            else:
                if num2[i] == key:
                    num2[i] = "0"
        

        return int("".join(num1)) - int("".join(num2))
