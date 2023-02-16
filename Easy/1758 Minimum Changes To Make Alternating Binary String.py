# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/


class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0

        
        flag1 = True
        flag2 = True
        for i in range(0, len(s)):
            if flag1:
                if s[i] != "0":
                    count1 += 1
                flag1 = False
            else:
                if s[i] != "1":
                    count1 += 1
                flag1 = True

        for i in range(0, len(s)):
            if flag2:
                if s[i] != "1":
                    count2 += 1
                flag2 = False
            else:
                if s[i] != "0":
                    count2 += 1
                flag2 = True


        print(count1, count2)   
        return min(count1, count2)
