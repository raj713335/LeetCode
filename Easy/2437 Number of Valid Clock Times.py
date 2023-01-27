# https://leetcode.com/problems/number-of-valid-clock-times/description/


class Solution:
    def countTime(self, time: str) -> int:

        combi = 1

        if time[0] == "?":
            try:
                if int(time[1]) > 3:
                    combi = 2
                else:
                    combi = 3
            except:
                pass

        
        if time[1] == "?":
            if time[0] == "?":
                combi = 24
            try:
                if int(time[0]) > 1:
                    combi = 4
                else:
                    combi = 10
            except:
                pass

        if time[3] == "?":
            combi *= 6
        
        if time[4] == "?":
            combi *= 10

        return combi

        
