# https://leetcode.com/problems/concatenated-words/description/

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        word_set = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set:
                    if suffix in word_set or dfs(suffix):
                        memo[word] = True
                        return True
            memo[word] = False
            return False

        result = []
        for word in words:
            if word == "":
                continue
            word_set.remove(word)  # avoid using itself
            if dfs(word):
                result.append(word)
            word_set.add(word)  # put it back for the next word

        return result
        
