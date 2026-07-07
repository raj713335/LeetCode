# https://leetcode.com/problems/unique-word-abbreviation/description/


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):

        self.words = defaultdict(list)

        for word in dictionary:
            self.words[ word[0] + str(len(word) -2) + word[-1]  ].append(word)
        

    def isUnique(self, word: str) -> bool:
        
        if word[0] + str(len(word) -2) + word[-1]  in self.words:
            for w in self.words[ word[0] + str(len(word) -2) + word[-1]  ]:
                if not w == word: return False
        return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
