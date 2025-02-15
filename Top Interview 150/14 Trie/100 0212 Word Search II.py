# https://leetcode.com/problems/word-search-ii/description/


class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        R = len(board)
        C = len(board[0])

        root = TrieNode()


        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

            curr.endOfWord = True

        curr = root

        visited, res = set(), set()
        def dfs(r, c, word, curr):

            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or board[r][c] not in curr.children:
                return 

        
            visited.add((r,c))
            word += board[r][c]
            curr = curr.children[board[r][c]]

            if curr.endOfWord == True:
                res.add(word)

            dfs(r + 1, c, word, curr)
            dfs(r - 1, c, word, curr)
            dfs(r, c + 1, word, curr)
            dfs(r, c - 1, word, curr)


            visited.remove((r,c))


        for i in range(0, R):
            for j in range(0, C):
                dfs(i, j, "", curr)

        return list(res)
