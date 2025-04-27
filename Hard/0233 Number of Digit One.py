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



class Solution:
    def countDigitOne(self, n: int) -> int:

        def count_ones(x):
            # Base case
            if x <= 0:
                return 0
            
            # We will find how many times 1 appears in all digits from 0 to x.
            # For example, for x = 234, we want to count how many 1's appear in the
            # units place, tens place, hundreds place, and so on.
            
            # Convert number to string to get the length
            s = str(x)
            length = len(s)
            first_digit = int(s[0])
            remaining_digits = int(s[1:]) if length > 1 else 0
            
            # Count the number of ones in the first digit
            count = 0
            # If the first digit is greater than 1, we can count 1 for all remaining combinations
            if first_digit > 1:
                count += (10 ** (length - 1)) * first_digit
            # If the first digit is exactly 1, count all numbers starting from the remaining part
            elif first_digit == 1:
                count += remaining_digits + 1
            # Count ones in the lower digits recursively
            count += count_ones(remaining_digits) + (first_digit * (length - 1) * 10 ** (length - 2))
            
            return count
        
        return count_ones(n)

        
