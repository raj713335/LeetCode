# https://leetcode.com/problems/fruit-into-baskets/description/


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        dictx = {}

        max_fruit = 0
        count = 0

        i = 0
        j = 0
        while i < len(fruits):
            
            if fruits[i] not in dictx:
                dictx[fruits[i]] = 1
                count += 1

                if len(dictx.keys()) > 2:
                    flag = True
                    while flag:
                        dictx[fruits[j]] -= 1
                        if dictx[fruits[j]] == 0:
                            del dictx[fruits[j]]
                        
                        count -= 1
                        j += 1
                        if len(dictx.keys()) <= 2:
                            flag = False
                else:
                    if count > max_fruit:
                        max_fruit = count



            else:
                dictx[fruits[i]] += 1
                count += 1

            
            i += 1
            if count > max_fruit:
                max_fruit = count

        return max_fruit
