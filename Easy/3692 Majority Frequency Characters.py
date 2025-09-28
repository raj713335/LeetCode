# https://leetcode.com/problems/majority-frequency-characters/description/


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:

        dictx = {}

        for num in s:
            if num not in dictx.keys():
                dictx[num] = 1
            else:
                dictx[num] += 1


        result_dictx = {}

        for key, value in dictx.items():
            if value not in result_dictx.keys():
                result_dictx[value] = [key]
            else:
                result_dictx[value].append(key)


        majority = ""
        freq = 0
        max_majority = 0

        for key, values in result_dictx.items():
            if len(values) > max_majority:
                max_majority = len(values)
                majority = values
                freq = key
            elif len(values) == max_majority and key > freq:
                max_majority = len(values)
                majority = values
                freq = key

        return "".join(majority)
        
