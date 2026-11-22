# https://leetcode.com/problems/assign-umbrella-on-rainy-days/description/

class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:

        umbrella = []

        alice = 0
        bob = 0

        for i in range(0, len(rain)-1):
            alice_flag = False
            bob_flag = False
            if rain[i] == 0:
                umbrella.append("None")
            if rain[i] == 1 and rain[i+1] == 1:
                alice_flag = True
            if rain[i] == 1:
                bob_flag = True

            if alice_flag == True and bob_flag == True:
                if alice <= bob:
                    alice += 1
                    umbrella.append("Alice") 
                else:
                    bob += 1
                    umbrella.append("Bob")
            elif bob_flag == True:
                bob += 1
                umbrella.append("Bob")

        if rain[-1] == 0:
            umbrella.append("None")
        else:
            umbrella.append("Bob")


        return umbrella
        
