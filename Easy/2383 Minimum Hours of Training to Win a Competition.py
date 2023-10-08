# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/description/

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:

        train_time = 0

        for i in range(len(energy)):
            if initialEnergy > energy[i] and initialExperience > experience[i]:
                initialEnergy -= energy[i]
                initialExperience += experience[i]
            else:
                if initialEnergy <= energy[i]:
                    while initialEnergy <= energy[i]:
                        initialEnergy += 1
                        train_time += 1
                if initialExperience <= experience[i]:
                    while initialExperience <= experience[i]:
                        initialExperience += 1
                        train_time += 1
                if initialEnergy > energy[i] and initialExperience > experience[i]:
                    initialEnergy -= energy[i]
                    initialExperience += experience[i]

        return train_time  

        
