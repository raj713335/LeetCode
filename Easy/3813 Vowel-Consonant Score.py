# https://leetcode.com/problems/vowel-consonant-score/description/


class Solution:
    def vowelConsonantScore(self, s: str) -> int:

        vowels = 0
        consonants = 0

        for word in s:
            if word in ["a", "e", "i", "o", "u"]:
                vowels += 1
            elif word in [
                "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
            ]:
                consonants += 1
        
        try:
            score = math.floor(vowels/consonants)
        except:
            score = 0

        return score
        
