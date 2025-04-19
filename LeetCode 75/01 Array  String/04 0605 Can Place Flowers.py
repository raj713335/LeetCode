# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 or n == 0:
                if n <= 1 or n == 0:
                    return True
                else:
                    return False
            else:
                return False

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                count += 1

        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerbed[-1] = 1
            count += 1

        print(flowerbed)

        if count >= n:
            return True
        else:
            return False
