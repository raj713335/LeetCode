# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/


class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(curr, index):
            if index == len(word):
                return curr.endOfWord 

            c = word[index]

            if c == ".":  
                for child in curr.children.values():
                    if dfs(child, index + 1): 
                        return True
                return False

            else: 
                if c not in curr.children:
                    return False
                return dfs(curr.children[c], index + 1)

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
