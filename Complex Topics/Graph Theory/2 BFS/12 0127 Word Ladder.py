# https://leetcode.com/problems/word-ladder/description/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        n = len(beginWord)

        q = deque()
        q.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        word_mutations = set(list("".join(wordList)))
        wordList = set(wordList)

        while q:

            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(0, n):
                mutates_endWord = word
                for each in word_mutations:
                    mutates_word = list(mutates_endWord)
                    mutates_word[i] = each
                    mutates_modified_word = "".join(mutates_word)
                    if mutates_modified_word in wordList and mutates_modified_word not in visited:
                        visited.add(mutates_modified_word)
                        q.append((mutates_modified_word, steps + 1))

        return 0
        
