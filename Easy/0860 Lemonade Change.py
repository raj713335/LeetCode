# https://leetcode.com/problems/lemonade-change/description/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = { "5": 0, "10": 0, "20": 0}

        for each in bills:
            if each == 5:
                change["5"] += 1
            elif each == 10:
                if change["5"] > 0:
                    change["5"] -= 1
                    change["10"] += 1
                else:
                    return False
            else:
                if change["10"] > 0:
                    if change["5"] > 0:
                        change["10"] -= 1
                        change["5"] -= 1
                        change["20"] += 1
                    else:
                        return False
                else:
                    if change["5"] >= 3:
                        change["5"] -= 3
                        change["20"] += 1
                    else:
                        return False
        
        return True
                
        
