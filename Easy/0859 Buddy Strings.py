# https://leetcode.com/problems/buddy-strings/description/


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        s = list(s)
        goal = list(goal)

        index = []
        mado = {}

        if len(s) != len(goal):
            return False


        for i in range(0, len(goal)):
            if goal[i] != s[i]:
                index.append(i)
            if goal[i] not in mado:
                mado[goal[i]] = 1
            else:
                mado[goal[i]] += 1


        if len(index) != 2:
            if len(index) == 0:
                if max(mado.values()) >= 2:
                    return True
            return False

        s[index[0]], s[index[1]] = s[index[1]], s[index[0]]

        if s == goal:
            return True
        else:
            return False

        
