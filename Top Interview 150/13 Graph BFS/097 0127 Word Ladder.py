# https://leetcode.com/problems/word-ladder/description/


from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        n = len(beginWord)

        mutation = list(set("".join(wordList)))
        wordList = set(wordList)
        
        q = deque()
        q.append([beginWord, 1])

        visited = set()

        while q:

            word, moves = q.popleft()

            if word == endWord:
                return moves

            for i in range(0, n):
                word_list = list(word)
                for m in mutation:
                    word_list[i] = m

                    word_str = "".join(word_list)

                    if word_str not in visited and word_str in wordList:
                        visited.add(word_str)
                        q.append([word_str, moves + 1]) 

        return 0
