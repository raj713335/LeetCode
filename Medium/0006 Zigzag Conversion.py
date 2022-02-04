#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""

        list = ["" for x in range(numRows)]

        #print(list)

        length = len(s)
        iter = 0
        i = 0
        flag = False

        while (length!=0):

            if iter<numRows and flag!= True:
                list[iter]+= s[i]
                i+=1
                iter+=1
                length-=1
                if iter == numRows-1:
                    flag = True

            elif flag==True:

                list[iter]+= s[i]
                iter -= 1
                i+=1
                length -= 1


                if iter== 0:
                    flag = False


            #print(list)




        return "".join(list)

        
