# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(0, len(image)):
            temp = image[i][::-1]
            for j in range(0, len(temp)):
                if temp[j] == 0:
                    temp[j] = 1
                else:
                    temp[j] = 0
            image[i] = temp
        return image
                
            
        
        
        
