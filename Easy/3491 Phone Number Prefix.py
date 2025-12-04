# https://leetcode.com/problems/phone-number-prefix/description/

class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:

        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)):
                if i != j:
                    length = len(numbers[i])
                    if numbers[i] == numbers[j][:length]:
                        return False

        return True
