# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/




class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        lst=set()
        for i in range(len(s)-k+1):
            each_String_size_k = s[i:i+k]
            lst.add(each_String_size_k)
        if len(lst) == 2**k:
            return True
        else:
            return False
        
