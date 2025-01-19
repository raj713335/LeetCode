# https://leetcode.com/problems/implement-trie-prefix-tree/description/


class Trie:

    def __init__(self):
        self.listx = []
        

    def insert(self, word: str) -> None:
        self.listx.append(word)
        

    def search(self, word: str) -> bool:
        for each in self.listx:
            if each == word:
                return True

        return False
        

    def startsWith(self, prefix: str) -> bool:
        len_prefix = len(prefix)
        for each in self.listx:
            if each[:len_prefix] == prefix:
                return True

        return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
