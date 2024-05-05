# https://leetcode.com/problems/sentence-similarity/description/


from collections import defaultdict 

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        
        if len(sentence1) != len(sentence2):
            return False

        for a,b in zip(sentence1, sentence2):
            if a == b:
                continue
            if [a, b] in similarPairs:
                continue
            elif [b, a] in similarPairs:
                continue
            return False

        return True
        
