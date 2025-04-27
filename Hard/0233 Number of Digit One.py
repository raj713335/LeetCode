# https://leetcode.com/problems/number-of-digit-one/description/

class Solution:
    def countDigitOne(self, n: int) -> int:

        # Memoization dictionary
        memo = {}
        
        def count_ones(x):
            # Base case: if x is less than 0, there are no 1's
            if x < 0:
                return 0
            
            # If already computed, return the result from memo
            if x in memo:
                return memo[x]
            
            # The main logic to count 1's in the range [0, x]
            count = 0
            factor = 1  # This will represent the place value (1, 10, 100, etc.)
            
            while factor <= x:
                # Split the number into three parts:
                # 1. The part to the left of the current digit
                left = x // (factor * 10)
                # 2. The current digit
                current_digit = (x // factor) % 10
                # 3. The part to the right of the current digit
                right = x % factor
                
                # Count 1's contributed by the current digit place
                if current_digit == 0:
                    count += left * factor
                elif current_digit == 1:
                    count += left * factor + right + 1
                else:
                    count += (left + 1) * factor
                
                # Move to the next higher digit place
                factor *= 10
            
            # Memoize the result for the current x
            memo[x] = count
            return count
        
        # Call the function for n
        return count_ones(n)
        
