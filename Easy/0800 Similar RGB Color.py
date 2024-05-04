# https://leetcode.com/problems/similar-rgb-color/description/

class Solution:
    def similarRGB(self, color: str) -> str:

        # We first split color into an array containing its three two-letter parts
        # and convert each value to an int of base 16 (hexadecimal)
        
        color = [int(color[i:i+2], 16) for i in range(1, len(color), 2)]

        
        # How do we find the closest number which can be written in shorthand?
        # Well, let's look at the pattern: 0x11, 0x22, ..., 0xFF
        # We can see that all of these numbers are divisible by 0x11 (17 in decimal)
        
        # To minimize this difference, we divide the value of each color by 0x11, round it, and convert to hex
        # This produces a shorthand string like 0x1, 0x2, ..., 0xF
        # But we want to return the full string, so we take the 3rd char (1,2,...,F) and double it (11,22,...FF)
        
        # We concatenate these strings and add '#' to the front to make the full 7-character color, and then return this string
        
        return '#'+''.join([hex(round(c/int('0x11', 16)))[2]*2 for c in color])
        
