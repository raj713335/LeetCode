# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        dictx = {}

        for i in range(len(arr)):
            if arr[i] not in dictx.keys():
                dictx[arr[i]] = 1
            else:
                dictx[arr[i]] += 1

        listx = sorted(dictx.items(), key = lambda x: x[1])

        for i in range(0, len(listx)):
            listx[i] = list(listx[i])


        for i in range(0, k):
            if listx[0][1] == 1:
                del listx[0]
            else:
                listx[0][1] -= 1


        return len(listx)
