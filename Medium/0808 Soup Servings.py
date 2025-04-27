# https://leetcode.com/problems/soup-servings/description/

class Solution:
    def soupServings(self, n: int) -> float:

        # Memoization dictionary
        memo = {}

        # Recursion function to compute the probability
        def prob(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            # Check memoization table
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Calculate the probability for all 4 operations
            result = 0.25 * (
                prob(a - 100, b) +
                prob(a - 75, b - 25) +
                prob(a - 50, b - 50) +
                prob(a - 25, b - 75)
            )
            
            # Memoize the result
            memo[(a, b)] = result
            return result

        # Scale down the problem if n > 5000 to avoid large numbers and simplify the problem
        # As n can be very large, we need to adjust the problem to avoid too many recursive calls.
        if n > 5000:
            n = 5000
        
        # Start the recursive calculation
        return prob(n, n)
        
