# https://leetcode.com/problems/text-justification/description/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        output = []
        count = 0
        start, end = 0, 0

        for i in range(0, len(words)):
            if count == 0:
                count += len(words[i])
            else:
                count += len(words[i]) + 1

            if count > maxWidth:
                temp = ""
                end = i - 1
                count -= ((end - start) + len(words[i]) + 1)

                try:
                    div = (maxWidth - count) // (end - start)
                    rem = (maxWidth - count) % (end - start)

                    flag = 0
                    if rem > 0:
                        flag = 1

                    for j in range(start, end + 1):
                        temp += words[j] + (" " * (div + flag))
                        rem -= 1
                        if rem == 0:
                            flag = 0

                    temp = temp.strip()

                except:
                    div = (maxWidth - count)
                    rem = 0

                    for j in range(start, end + 1):
                        temp += words[j] + (" " * (div + rem))
                        rem = 0


                output.append(temp)

                start = i
                count = len(words[i])

        temp = ""
        end = len(words) -1

        for j in range(start, end + 1):
            temp += words[j] + " "

        valx = maxWidth - len(temp)
        temp += " " * valx

        if valx < 0:
            temp = temp[:-1]

        output.append(temp)

        return output
                    
                


