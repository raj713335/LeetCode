# https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        res = []

        def backtrack(index, path, value, last):
            if index == len(num):
                if value == target:
                    res.append(path)
                return

            for i in range(index + 1, len(num) + 1):
                temp_str = num[index:i]

                # Skip numbers with leading zeros
                if len(temp_str) > 1 and temp_str[0] == '0':
                    continue

                temp_val = int(temp_str)

                if index == 0:
                    backtrack(i, temp_str, temp_val, temp_val)
                else:
                    backtrack(i, path + '+' + temp_str, value + temp_val, temp_val)
                    backtrack(i, path + '-' + temp_str, value - temp_val, -temp_val)
                    backtrack(i, path + '*' + temp_str, value - last + last * temp_val, last * temp_val)

        backtrack(0, '', 0, 0)
        return res
        
