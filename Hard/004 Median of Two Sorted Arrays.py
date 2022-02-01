# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total_count = len(nums1) + len(nums2)
        flag = False
        
        listx =[]
        
        if total_count % 2 == 0:
            val = total_count // 2
            flag = True
            count = -1
        else:
            val = math.ceil(total_count/2)
            count = 0
            

        i,j = 0,0
        
        while (i< len(nums1) and j <len(nums2)):
            if nums1[i] < nums2[j]:
                listx.append(nums1[i])
                count+=1
                i += 1
            else:
                listx.append(nums2[j])
                count += 1
                j += 1
            if count == val:
                if flag == False:
                    return listx[-1]
                else:
                    return ((listx[-1]+listx[-2])/2)
                
        while(i< len(nums1) and j == len(nums2)):
            listx.append(nums1[i])
            count += 1
            i += 1
            if count == val:
                if flag == False:
                    return listx[-1]
                else:
                    return ((listx[-1]+listx[-2])/2)
            
                
        while(i== len(nums1) and j < len(nums2)):
            listx.append(nums2[j])
            count += 1
            j += 1
            if count == val:
                if flag == False:
                    return listx[-1]
                else:
                    return ((listx[-1]+listx[-2])/2)
            
            
            
        
        
