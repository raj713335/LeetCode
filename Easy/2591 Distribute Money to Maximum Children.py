# https://leetcode.com/problems/distribute-money-to-maximum-children/description/


class Solution:
    def distMoney(self, money: int, children: int) -> int:


        ans = 0

        if money < children:
            return -1

        if money > children * 8:
            return children -1
        
        while money > 0 and money - 8 >= children -1:
            ans += 1
            money -= 8
            children -= 1

        if money == 4 and children == 1:
            ans -= 1
        
        return ans

        
