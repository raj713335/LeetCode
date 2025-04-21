# https://www.geeksforgeeks.org/problems/boolean-parenthesization5610/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card


#User function Template for python3
class Solution:
    def countWays(self, s):
        memo = {}

        def ways(i, j, isTrue):
            if i > j:
                return 0
            if i == j:
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0

            if (i, j, isTrue) in memo:
                return memo[(i, j, isTrue)]

            ans = 0
            for k in range(i + 1, j, 2):  # operator position
                op = s[k]

                LT = ways(i, k - 1, True)
                LF = ways(i, k - 1, False)
                RT = ways(k + 1, j, True)
                RF = ways(k + 1, j, False)

                if op == '&':
                    if isTrue:
                        ans += LT * RT
                    else:
                        ans += LT * RF + LF * RT + LF * RF
                elif op == '|':
                    if isTrue:
                        ans += LT * RT + LT * RF + LF * RT
                    else:
                        ans += LF * RF
                elif op == '^':
                    if isTrue:
                        ans += LT * RF + LF * RT
                    else:
                        ans += LT * RT + LF * RF

            memo[(i, j, isTrue)] = ans
            return ans
            
        return ways(0, len(s) - 1, True)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends
