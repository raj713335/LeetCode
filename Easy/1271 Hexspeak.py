# https://leetcode.com/problems/hexspeak/description/

class Solution:
    def toHexspeak(self, num: str) -> str:

        Hexspeak = hex(int(num))[2:].upper()

        Hexspeak = Hexspeak.replace("1", "I")
        Hexspeak = Hexspeak.replace("0", "O")
        
        for h in Hexspeak:
            if h not in "ABCDEFIO":
                return "ERROR"

        return Hexspeak 
        
