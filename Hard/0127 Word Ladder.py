# https://leetcode.com/problems/word-ladder/description/


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = set(list("".join(wordList)))
        wordList = set(wordList)
        
        q = collections.deque()
        q.append([beginWord, 1])

        n = len(beginWord)

        visited = set()

        while q:
            word, move = q.popleft()
            visited.add(word)
            for i in range(0, n):
                mutation_word = word
                for each in words:
                    mutation_word = list(mutation_word)
                    mutation_word[i] = each
                    mutation_word = "".join(mutation_word)
                    if mutation_word in wordList  and mutation_word not in visited:
                        if mutation_word == endWord:
                            return move + 1
                        q.append([mutation_word, move+1])
        return 0
        
