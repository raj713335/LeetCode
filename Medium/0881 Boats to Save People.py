# https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people = sorted(people)
        count = 0
        

        while len(people) > 0:

            i = -1

            more_to_add = limit - people[i]

            value = -1

            for i in range(0, len(people)-1):
                if more_to_add >= people[i]:
                    value = i
                else:
                    break

            if value != -1:
                del people[value]

            del people[-1]
            count += 1

        return count
                

