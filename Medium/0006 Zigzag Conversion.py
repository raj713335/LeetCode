#https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        list = ["" for x in range(numRows)]

        iterx = 0
        i = 0
        flag =False
        
        while(i!=len(s)):
            
            if iterx < numRows and flag!= True:
                list[iterx]+= s[i]
                i+= 1
                iterx+=1
           
                if iterx == numRows-1:
                    flag = True
                
            elif flag == True:

                list[iterx]+=s[i]
                iterx -=1
                i+=1


                if iterx ==0:
                    flag = False
                        
        return "".join(list)
        
