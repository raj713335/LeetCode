# https://leetcode.com/problems/shortest-common-supersequence/description/


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
        
