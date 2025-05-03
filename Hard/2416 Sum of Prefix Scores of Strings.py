# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Trie():
    def __init__(self):
        self.children = {}
        self.count = 0
        self.endOfWord = False


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        root = Trie()

        for word in words:
            curr = root
            for pa in word:
                if pa not in curr.children:
                    curr.children[pa] = Trie()
                
                curr = curr.children[pa]
                curr.count += 1
            curr.endOfWord = True

        res = []

        for word in words:
            curr = root
            total = 0
            for pa in word:
                curr = curr.children[pa]
                total += curr.count

            res.append(total)

        return res

