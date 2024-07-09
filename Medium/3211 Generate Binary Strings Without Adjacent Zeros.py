# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/


from itertools import product

class Solution:
    def validStrings(self, n: int) -> List[str]:

        if n == 1:
            return ["0", "1"]

        values = list(product(["0", "1"], repeat=n))
        res = []

        for each in values:
            count_1 = False
            temp = "".join(each)
            if temp[0] == "1":
                count_1 = True
            for i in range(1, n):
                if temp[i-1] == temp[i] and temp[i] == "0":
                    count_1 = False
                    break
                elif temp[i] == "1":
                    count_1 = True
            if count_1:
                res.append(temp)

        return res
