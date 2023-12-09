# https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/

from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:

        freq = Counter(word).values()
        mi, ma, le, wle = min(freq), max(freq), len(freq), len(word)
        return (
                le == 1 or  # one char any times
                ma == 1 or  # each char once
                mi == ma - 1 and wle == mi * le + 1 or  # one char extra
                mi == 1 and wle == ma * (le - 1) + 1  # single extra char
        )
