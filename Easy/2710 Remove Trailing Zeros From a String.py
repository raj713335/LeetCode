# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/


class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        num = list(num)
        for i in range(len(num)-1, -1, -1):
            if num[i] == "0":
                del num[i]
            else:
                break

        return "".join(num)
