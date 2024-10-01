# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/?envType=daily-question&envId=2024-10-01


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        rem_val = defaultdict(int)

        for i in range(0, len(arr)):
            rem = arr[i] % k
            rem_val[rem] += 1

        if rem_val[0] % 2 != 0:
                return False

        for i in range(1, (k//2) + 1):
            if rem_val[i] != rem_val[k-i]:
                return False

        return True
