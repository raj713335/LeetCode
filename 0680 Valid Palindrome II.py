# https://leetcode.com/problems/valid-palindrome-ii/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        length = len(s)
        
        low = 0
        high = length-1
        counter = 0
        
        
        while low < high:
            print(s[low] ,s[high])
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                try:
                    if s[low+1] == s[high] and s[low+2] == s[high-1]:
                        low += 1
                    else:
                        high -= 1
                except:
                    high -= 1
                
                counter += 1
                
                
        low = 0
        high = length-1
        counter1 = 0
        
        print(" ")
        
        
        while low < high:
            print(s[low] ,s[high])
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                try:
                    if s[low] == s[high-1] and s[low+1] == s[high-2]:
                        high -= 1
                    else:
                        low += 1
                except:
                    low += 1
                
                counter1 += 1

                
        if min(counter,counter1) > 1:
            return False
        
        return True
                    
                
                
        
