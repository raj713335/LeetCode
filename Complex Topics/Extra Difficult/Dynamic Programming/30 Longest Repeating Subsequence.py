# Python program to find longest
# repeating subsequence using recursion
  

def findLongestRepeatingSubsequence(i, j, s):

    # base case
    if i == 0 or j == 0:
        return 0

    # If characters match and their
    # indices are different
    if s[i - 1] == s[j - 1] and i != j:
        return 1 + findLongestRepeatingSubsequence(i - 1, j - 1, s)

    # Else make two recursive calls.
    return max(findLongestRepeatingSubsequence(i - 1, j, s),
               findLongestRepeatingSubsequence(i, j - 1, s))


def longestRepeatingSubsequence(s):
    n = len(s)
    return findLongestRepeatingSubsequence(n, n, s)


if __name__ == "__main__":
    s = "AABEBCDD"
    res = longestRepeatingSubsequence(s)
    print(res)
