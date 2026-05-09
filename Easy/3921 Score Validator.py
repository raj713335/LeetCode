# https://leetcode.com/problems/score-validator/description/

class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:

        counter = 0
        score = 0

        for each in events:
            if each == "W":
                counter += 1
            elif each == "WD" or each == "NB":
                score += 1
            else:
                score += int(each)

            if counter == 10:
                break

        return [score, counter]
        
