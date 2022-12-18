# https://leetcode.com/problems/calculate-amount-paid-in-taxes/description/

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        tax_cost = 0
        i = 1

        if income >= brackets[0][0]:
            tax_cost += ((brackets[0][0] * brackets[0][1])/100) 
            income -= brackets[0][0] 
        else:
            tax_cost += ((income * brackets[0][1])/100) 
            income = 0



        while income > 0 and i < len(brackets):
            sub_income = (brackets[i][0] - brackets[i-1][0])

            if income >= sub_income:
                tax_cost += ((sub_income * brackets[i][1])/100) 
            else:
                tax_cost += ((income * brackets[i][1])/100) 
            income -= sub_income
            i+= 1

        if income > 0:
            tax_cost += ((income * brackets[-1][1])/100) 





        return tax_cost

        

        
        
