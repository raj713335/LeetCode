# https://leetcode.com/problems/largest-number-after-mutating-substring/description/


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:

        num = list(num)
        print(num)

        res = ""

        for i in range(0, len(num)):
            if int(num[i]) < change[int(num[i])]:
                num[i] = str(change[int(num[i])])
                j = i+1
                while j < len(num):
                    if int(num[j]) <= change[int(num[j])]:
                        num[j] = str(change[int(num[j])])
                        j += 1
                    else:
                        break

                return "".join(num)

        
        return "".join(num)
