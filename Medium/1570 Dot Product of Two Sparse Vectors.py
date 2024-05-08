# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/

class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.dict[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        if not self.dict or not vec.dict:
            return 0
        low, high = min(self.dict.keys()), max(self.dict.keys()) 
        for i in range(low, high+1):
            if (i in self.dict) and (i in vec.dict):
                result += self.dict[i] * vec.dict[i]
        return result

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
