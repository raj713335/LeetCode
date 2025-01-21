# https://leetcode.com/problems/word-search-ii/description/

class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or board[r][c] not in node.children:
                return

            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.endOfWord == True:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        node = root

        for r in range(0, ROWS):
            for c in range(0, COLS):
                dfs(r, c, node, "")
        
        return list(res)

        
        
        
