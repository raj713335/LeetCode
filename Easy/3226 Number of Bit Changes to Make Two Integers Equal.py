# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/description/

class Solution:
    def minChanges(self, n: int, k: int) -> int:


        n = bin(n)[2:]
        k = bin(k)[2:]

        n_len = len(n)
        k_len = len(k)

        count = 0

        if n_len > k_len:
            k = ("0" * n_len + k[:])[-n_len:]
        else:
            n = ("0" * k_len + n[:])[-k_len:]


        for i in range(0, n_len):
            if n[i] != k[i] and n[i] == "1":
                count += 1
            elif n[i] != k[i]:
                return -1

        return count
