# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums = sorted(nums)

        org_queries = queries

        queries = sorted(queries)

        queries_dict = {}

        ans = []

        sumx = 0
        count = 0

        i = 0
        j = 0
        last = 0

        while i < len(queries):

            if sumx > queries[i]:
                #print(sumx)
                count -= 1
                sumx -= last
                last = 0
                j -= 1
                queries_dict[queries[i]] = count
                i += 1
            else:
                if j == len(nums):
                    queries_dict[queries[i]] = count
                    i += 1
                else:
                    sumx += nums[j]
                    last = nums[j]
                    count += 1
                    j += 1

        for each in org_queries:
            ans.append(queries_dict[each])

        return ans
