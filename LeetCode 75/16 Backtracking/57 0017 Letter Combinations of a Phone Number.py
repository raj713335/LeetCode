# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        n = len(digits)

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

        def backtrack(index, substring):

            if n == len(substring):
                res.append(substring)
                return 

            for s in char_to_number[digits[index]]:
                backtrack(index+1, substring+s)

        backtrack(0, "")

        if not digits:
            return []
            
        return res