# https://leetcode.com/problems/coupon-code-validator/description/

import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        allowed_lines = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        valid = []

        for i in range(len(code)):
            c = code[i]
            b = businessLine[i]
            a = isActive[i]

            # Check 1: code is non-empty and only alphanumeric or underscore
            if not c or not re.fullmatch(r"[A-Za-z0-9_]+", c):
                continue

            # Check 2: business line is allowed
            if b not in allowed_lines:
                continue

            # Check 3: must be active
            if not a:
                continue

            # If valid, store (category index, code)
            valid.append((allowed_lines[b], c))

        # Sort by (businessLine index, code)
        valid.sort()

        # Return only the codes
        return [c for _, c in valid]
        
