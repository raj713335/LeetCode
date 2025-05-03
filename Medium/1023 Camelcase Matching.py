# https://leetcode.com/problems/camelcase-matching/description/

class Trie():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        root = Trie()

        curr = root

        for pa in pattern:
            if pa not in curr.children:
                curr.children[pa] = Trie()
            curr = curr.children[pa]
        curr.endOfWord = True

        res = []

        for qa in queries:
            curr = root
            n = len(qa)

            for word in qa:
                if word in curr.children:
                   curr = curr.children[word]
                   n -= 1 
                   continue
                elif word.isupper():
                    n = -1
                    break
                else:
                    n -= 1
            
            if n == 0 and curr.endOfWord:
                res.append(True)
            else:
                res.append(False)
        
        return res
