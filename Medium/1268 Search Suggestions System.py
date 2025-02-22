# https://leetcode.com/problems/search-suggestions-system/description/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        res = []
        products.sort()

        l, r = 0, len(products) - 1

        for i in range(0, len(searchWord)):
            c = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1

            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            res.append([])
            remain = r - l + 1
            for j in  range(min(3, remain)):
                res[-1].append(products[l+j])
        
        return res


# with Prefix Tree  


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
