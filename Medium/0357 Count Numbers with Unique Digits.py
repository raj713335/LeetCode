# https://leetcode.com/problems/count-numbers-with-unique-digits/description/


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        # Memoization dictionary to store intermediate results
        memo = {}

        def count(k):
            # Base case: if k == 0, there's only one valid number: 0
            if k == 0:
                return 1
            # Base case: if k == 1, there are 10 valid numbers (0 to 9)
            if k == 1:
                return 10
            
            # Check if the result is already computed for k
            if k in memo:
                return memo[k]
            
            # Recursively calculate the number of valid numbers with k digits
            # For k digits, the first digit can be chosen in 9 ways (1-9)
            # The second in 9 ways (0-9, but not the first digit)
            # The third in 8 ways, and so on
            product = 9
            for i in range(9, 9 - k + 1, -1):
                product *= i

            # Memoize the result for k digits
            memo[k] = product + count(k - 1)  # Add result for (k-1) digits

            return memo[k]

        # The result is the sum of valid numbers with 1 to n digits
        return count(n)


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        # Base case when n == 0
        if n == 0:
            return 1

        # Start by calculating the unique numbers for each digit length 1 to n
        result = 10  # For n = 1, all numbers from 0 to 9 are valid
        product = 9  # For n = 1, the first digit can be any of 9 (1 to 9)

        # For each subsequent number length from 2 to n
        for i in range(2, n + 1):
            product *= (11 - i)  # (10 - i) gives us the count of available digits for each position
            result += product  # Add the count of valid numbers with i digits

        return result
