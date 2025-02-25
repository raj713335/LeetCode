# https://leetcode.com/problems/word-search/description/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R, C = len(board), len(board[0])

        visited = set()

        def dfs(r, c, substring, index):

            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or board[r][c] != word[index]:
                return False

            substring += board[r][c]
            index += 1

            if substring == word:
                return True

            visited.add((r, c))

            res = dfs(r + 1, c, substring, index) or dfs(r - 1, c, substring, index) or dfs(r, c + 1, substring, index) or dfs(r, c - 1, substring, index)

            visited.remove((r, c))

            return res


        for i in range(0, R):
            for j in range(0, C):
                if dfs(i, j, "", 0):
                    return True

        return False
        
