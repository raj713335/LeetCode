# https://leetcode.com/problems/random-pick-with-weight/description/


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        # Generate a random number in the range [1, total_sum]
        random_num = random.randint(1, self.total_sum)
        # Use binary search to find the index of the random number in prefix_sum
        index = bisect_left(self.prefix_sum, random_num)
        # Return the index corresponding to the random number
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
