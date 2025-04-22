# https://leetcode.com/problems/search-suggestions-system/description/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        root = TrieNode()

        products = sorted(products)

        for word in products:
            curr = root
            for w in word:
                if w not in curr.children:
                    curr.children[w] = TrieNode()
                curr = curr.children[w]
                if len(curr.suggestions) < 3:
                    curr.suggestions.append(word)


        res = [[] for char in searchWord]
        
        curr = root
        for i, w in enumerate(searchWord):
            if w not in curr.children:
                break
            curr = curr.children[w]
            res[i] = curr.suggestions

        return res