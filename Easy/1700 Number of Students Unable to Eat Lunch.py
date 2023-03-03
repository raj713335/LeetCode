# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        flag = True
        count = 0

        while flag:
            x = students.pop(0)
            y = sandwiches.pop(0)

            if x == y:
                count = 0
            else:
                students.append(x)
                sandwiches.insert(0, y)
                count += 1

            if count == len(students)+1 or len(students) == 0:
                return len(students)



        
