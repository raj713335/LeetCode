# https://leetcode.com/problems/palindrome-partitioning-ii/description/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
    
        # Precompute palindrome table
        is_palindrome = [[False]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_palindrome[i+1][j-1]):
                    is_palindrome[i][j] = True

        memo = {}

        def dfs(i):
            if i == n:
                return -1  # no cuts needed if we're done
            if i in memo:
                return memo[i]
            
            min_cuts = float('inf')
            for j in range(i, n):
                if is_palindrome[i][j]:
                    cuts = 1 + dfs(j+1)
                    min_cuts = min(min_cuts, cuts)
            
            memo[i] = min_cuts
            return min_cuts
        
        return dfs(0)



# Normal Method 

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = {}

        # Step 1: Precompute all palindrome substrings
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or is_palindrome[i + 1][j - 1]:
                        is_palindrome[i][j] = True

        # Step 2: Recursive function with memoization
        def dfs(start):
            if start == n:
                return 0
            if start in dp:
                return dp[start]

            min_cuts = float('inf')
            for end in range(start, n):
                if is_palindrome[start][end]:
                    cuts = 1 + dfs(end + 1)
                    min_cuts = min(min_cuts, cuts)

            dp[start] = min_cuts
            return dp[start]

        return dfs(0) - 1


# MCM Not working Yet 

class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        dp = {}

        def isPalindrome(s, i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
                
            return True

        def solve(s, i, j):
            if i >= j:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            ans = float("inf")

            if isPalindrome(s, i, j):
                dp[(i, j)] = 0
                return 0

            for k in range(i, j):
                #temp = solve(s, i, k) + solve(s, k+1, j) + 1

                if (i, k) not in dp:
                    left =  solve(s, i, k)
                else:
                    left = dp[(i, k)]
                    dp[(i, j)] = left

                if (k+1, j) not in dp:
                    right = solve(s, k+1, j)
                    dp[(i, j)] = right
                else:
                    right = dp[(k+1, j)]

                temp = left + right + 1
                ans = min(ans, temp)

            dp[(i, j)] = ans
            return dp[(i, j)]


        return solve(s, 0, n-1)
        
