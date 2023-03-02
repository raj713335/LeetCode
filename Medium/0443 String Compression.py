# https://leetcode.com/problems/string-compression/description/


class Solution:
    def compress(self, chars: List[str]) -> int:

        prev = ""
        count = 0

        res = ""
        
        for i in range(0, len(chars)):
            if chars[i] != prev:
                if prev != "":
                    if count == 1:
                        res += prev
                    else:
                        res += prev + str(count)
                    
                prev = chars[i]
                count = 1
            else:
                count += 1

        if count == 1:
            res += prev
        else:
            res += prev + str(count)

        chars[:] = res

        return len(chars)
        
