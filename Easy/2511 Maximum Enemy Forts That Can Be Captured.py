# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/description/


class Solution:
    def captureForts(self, forts: List[int]) -> int:

        max_capture = 0
        flag = False
        temp = 0
        for i in range(0, len(forts)):
            if flag and forts[i] == 0:
                temp += 1
            elif forts[i] == 1:
                flag = True
                temp = 0
            elif forts[i] == -1:
                flag = False
                if temp > max_capture:
                    max_capture = temp
                    temp = 0

        

        for i in range(len(forts)-1, -1, -1):
            if flag and forts[i] == 0:
                temp += 1
            elif forts[i] == 1:
                flag = True
                temp = 0
            elif forts[i] == -1:
                flag = False
                if temp > max_capture:
                    max_capture = temp
                    temp = 0

        return max_capture
