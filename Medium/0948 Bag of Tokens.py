# https://leetcode.com/problems/bag-of-tokens/description/


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        tokens = sorted(tokens)
        i, j = 0, len(tokens) - 1
        score = 0

        if len(tokens) == 0 or power < tokens[0]:
            return 0

        while power > 0 or score > 0:
            if i > j:
                break
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                i += 1
            else:
                if tokens[j] > tokens[i]:
                    power += tokens[j]
                    score -= 1
                    j -= 1
                else:
                    break
        return score
