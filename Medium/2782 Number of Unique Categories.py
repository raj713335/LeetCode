# https://leetcode.com/problems/number-of-unique-categories/description/


# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:

        res = [0]

        for i in range(1, n):
            val = False
            for j in res:
                if categoryHandler.haveSameCategory(i, j):
                    val = True
                    break

            if not val:
                res.append(i)
        
        return len(res)
