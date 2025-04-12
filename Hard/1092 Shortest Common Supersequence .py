# https://leetcode.com/problems/shortest-common-supersequence/description/


## Bottom Up Approach 

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n = len(str1)
        m = len(str2)

        res = []

        dp = [[0] * (m + 1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i, j = n, m

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                res.append(str1[i-1])
                i -= 1
                j -= 1
        
            elif dp[i - 1][j] > dp[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1


        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return "".join(res[::-1])

        


## Recursive + Memoization Approach
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        @lru_cache(maxsize= 8000)
        def helper(first: str, second: str):
            
            if not first and not second:
                return ""
            
            if not first:
                return second
            
            if not second:
                return first
            
            if first[0] == second[0]:
                return first[0] + helper(first[1:], second[1:])
            
            right = second[0] + helper(first, second[1:])
            left = first[0] + helper(first[1:], second)
            
            if len(right) > len(left):
                return left
            return right
            
        return helper(str1, str2)


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        n1 =  len(str1) - 1
        n2 =  len(str2) - 1

        dp = {}

        def dfs(text1, text2, index_1, index_2):

            if index_1 == -1:
                return list(text2[:index_2 + 1])
            if index_2 == -1:
                return list(text1[:index_1 + 1])
            if (index_1, index_2) in dp:
                return dp[(index_1, index_2)]

            ways = ""

            if text1[index_1] == text2[index_2]:
                ways = dfs(text1, text2, index_1 - 1, index_2 - 1) + [text1[index_1]]

            else:
                way_1 = dfs(text1, text2, index_1 - 1, index_2) + [text1[index_1]]
                way_2 = dfs(text1, text2, index_1, index_2 - 1) + [text2[index_2]]

                n_way_1 = len(way_1)
                n_way_2 = len(way_2)
                
                if n_way_1 < n_way_2:
                    ways = way_1
                else:
                    ways = way_2


            dp[(index_1, index_2)] = ways
            return dp[(index_1, index_2)]

        return dfs(str1, str2, n1, n2)
        
