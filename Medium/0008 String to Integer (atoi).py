# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        
        pattern = re.compile(r'^[-|+]{0,1}[0-9]+\.{0,1}[0-9]*')
        # Since the .split() method splits the strings using whitespaces as separator,
        # if the input string is the empty string or a string with white spaces, we will
        # obtain an empty list, so we will not enter the if block. The second condition
        # checks if there is a matching pattern.

        if s.split() and pattern.search(s.split()[0]):
            if int(float(pattern.search(s.split()[0]).group())) > 2**31 - 1:
                return 2**31 - 1
            if int(float(pattern.search(s.split()[0]).group())) < -2**31:
                return -2**31
            return int(float(pattern.search(s.split()[0]).group()))
        return 0
    
"""
        pattern = re.compile("^[+|-]{0,1}[0-9]+\.{0,1}[0-9]*")

        try:
            ss = int(float(re.search(pattern, s.split()[0]).group()))

            if ss < -1*(2**31):
                return -1*(2**31)
            elif ss > (2**31 -1):
                return (2**31 -1)
            else:
                return ss

        except:
            return 0
"""

            
        
        
        
        
