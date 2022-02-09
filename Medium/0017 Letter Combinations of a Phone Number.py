
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []

        dictx = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        try:
            res = list(dictx[int(digits[0])])
        except:
            return []

        #print(res)

        for each in digits[1:]:
            res = self.combiation(dictx[int(each)], res)

        return res
    
    def combiation(self, list, result):
        res = []

        for i in result:
            for j in list:
                res.append(i + j)

        #print(res)
        return res

        
        
        
        
