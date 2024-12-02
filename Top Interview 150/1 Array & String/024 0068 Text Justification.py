# https://leetcode.com/problems/text-justification/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []
        word_length = 0
        temp_word =[]

        for i in range(0, len(words)):
            word_length += len(words[i])

            if word_length + len(temp_word) <= maxWidth:
                temp_word.append(words[i])
            else:
                res.append(temp_word)
                temp_word = []
                temp_word.append(words[i])
                word_length = len(words[i])


        for i in range(0, len(res)):
            length = maxWidth - len("".join(res[i]))
            length_word = len(res[i]) - 1
            
            try:
                spaces = length//length_word

                while length > 0:
                    for j in range(1, len(res[i])):

                        res[i][j] = " " * (spaces) + res[i][j]
                        length -= spaces

                        if length <= 0:
                            res[i][j] = res[i][j][abs(length):]
                            break

            except:
                res[i][0] = res[i][0] + " " * length

        res_string = []

        for each in res:
            res_string.append("".join(each))

        res_string.append(" ".join(temp_word))

        length = maxWidth - len(res_string[-1])
        res_string[-1] = res_string[-1] + " " * length

        return res_string
