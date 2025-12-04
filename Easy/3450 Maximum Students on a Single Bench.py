# https://leetcode.com/problems/maximum-students-on-a-single-bench/description/

class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:

        dictx = {}

        for student, bench in students:
            if bench not in dictx:
                dictx[bench] = [student]
            else:
                dictx[bench].append(student)

        max_students = 0

        for value in dictx.values():
            temp = len(set(value))

            if temp > max_students:
                max_students = temp

        return max_students
        
