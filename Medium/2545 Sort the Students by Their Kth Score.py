# https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        score = sorted(score, key= lambda x: x[k], reverse = True)

        return score
