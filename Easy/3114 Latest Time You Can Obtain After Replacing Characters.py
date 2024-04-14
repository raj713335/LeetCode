# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/description/

class Solution:
    def findLatestTime(self, s: str) -> str:

        hour, minute = s.split(":")

        hour = list(hour)
        minute = list(minute)

        if hour.count("?") == 2:
            hour = "11"
        elif hour.count("?") == 1:
            if hour[0] == "?":
                if int(hour[1]) > 1:
                     hour[0] = "0"
                else:
                    hour[0] = "1"
            else:
                if hour[0] == "0":
                    hour[1] = "9"
                else:
                    hour[1] = "1"

        if minute.count("?") == 2:
            minute = "59"
        elif minute.count("?") == 1:
            if minute[0] == "?":
                minute[0] = "5"
            else:
                minute[1] = "9"

        return "".join(hour) + ":" + "".join(minute)
                


        
