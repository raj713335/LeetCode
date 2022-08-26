# https://leetcode.com/problems/replace-words/


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        sentence = sentence.split(" ")
        dictionary = sorted(dictionary)
        
        for i in range(0, len(sentence)):
            for j in range(0, len(dictionary)):
                #print(dictionary[j],  sentence[i][0: len(dictionary[j])])
                if dictionary[j] == sentence[i][0: len(dictionary[j])]:
                    sentence[i] = dictionary[j]
                    break
                    
        return " ".join(sentence)
        
