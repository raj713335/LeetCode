# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        dictx = {}
        output = []

        for i in range(0, len(groupSizes)):
            if groupSizes[i] not in dictx:
                dictx[groupSizes[i]] = [i]
            else:
                dictx[groupSizes[i]].append(i)


        for each in sorted(dictx.keys()):
            container = []
            i = 0
            flag = True
            for val in dictx[each]:
                container.append(val)
                i += 1
                flag = True

                if i == each:
                    output.append(container)
                    i = 0
                    container = []
                    flag = False
            if flag:
                output.append(container)

        return output
        
