# https://leetcode.com/problems/guess-number-higher-or-lower/


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        lowerBound, upperBound = 1, n
        myGuess = (lowerBound+upperBound) // 2
        

        while (res := guess(myGuess)) != 0:
            if res == 1:
                lowerBound = myGuess+1
            else:
                upperBound = myGuess-1
            myGuess = (lowerBound+upperBound) // 2

        return myGuess
        
