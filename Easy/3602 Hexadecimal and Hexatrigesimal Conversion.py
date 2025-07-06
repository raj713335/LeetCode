# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/description/

class Solution:
    def concatHex36(self, n: int) -> str:

        def to_base(num, base, digits):
            if num == 0:
                return "0"
            result = ""
            while num > 0:
                result = digits[num % base] + result
                num //= base
            return result

        hex_digits = "0123456789ABCDEF"
        base36_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        n_squared = n * n
        n_cubed = n * n * n

        hex_part = to_base(n_squared, 16, hex_digits)
        base36_part = to_base(n_cubed, 36, base36_digits)

        return hex_part + base36_part
        
