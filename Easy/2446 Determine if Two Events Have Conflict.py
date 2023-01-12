# https://leetcode.com/problems/determine-if-two-events-have-conflict/description/


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        if event1[0].split(":")[0] > event2[0].split(":")[0]:
            a,b = event2[1].split(":")
            c,d = event1[0].split(":")
        elif event1[0].split(":")[0] < event2[0].split(":")[0]:
            a,b = event1[1].split(":")
            c,d = event2[0].split(":")
        else:
            if event1[0].split(":")[1] >= event2[0].split(":")[1]:
                a,b = event2[1].split(":")
                c,d = event1[0].split(":")
            else:
                a,b = event1[1].split(":")
                c,d = event2[0].split(":")



        if int(a) > int(c):
            return True

        if int(a) == int(c):
            if int(b) >= int(d):
                return True



        return False
        
