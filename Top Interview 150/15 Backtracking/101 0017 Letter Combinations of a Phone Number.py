# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []

        char_to_number = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtracking(index, substr):
            if len(digits) == len(substr):
                res.append(substr)
                return 

            for s in char_to_number[digits[index]]:
                backtracking(index+1, substr+s)

        if digits:
            backtracking(0, "")

        return res
        
