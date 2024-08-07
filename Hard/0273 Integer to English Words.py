# https://leetcode.com/problems/integer-to-english-words/description

class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }

        tens_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        postfix = ["", " Thousand", " Million", " Billion"]

        def get_string(n):
            res = []
            hundreds = n // 100
            if hundreds:
                res.append(ones_map[hundreds] + " Hundred")
            last_2 = n % 100
            if last_2 >= 20:
                tens, ones = last_2 // 10, last_2 % 10
                res.append(tens_map[tens * 10])
                if ones:
                    res.append(ones_map[ones])

            elif last_2:
                res.append(ones_map[last_2])
            
            return " ".join(res)

        i = 0
        res = []
        while num:
            digits = num % 1000
            s = get_string(digits)
            if s:
                res.append(s + postfix[i])
            num = num // 1000
            i += 1
        res.reverse()

        return " ".join(res)
        
