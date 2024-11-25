
def isAllStars(S1, i):
    # Helper function to check if all characters up to index i in S1 are '*'
    for j in range(i + 1):
        if S1[j] != '*':
            return False
    return True

def wildcardMatchingUtil(S1, S2, i, j, dp):
    # Base conditions
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= 0:
        return False
    if j < 0 and i >= 0:
        return isAllStars(S1, i)

    # If the result for this subproblem is already computed, return it
    if dp[i][j] != -1:
        return dp[i][j]

    if S1[i] == S2[j] or S1[i] == '?':
        # Characters match or S1 has a '?'; move to the previous characters in both strings
        dp[i][j] = wildcardMatchingUtil(S1, S2, i - 1, j - 1, dp)
    elif S1[i] == '*':
        # If S1 has a '*', there are two choices:
        # 1. '*' represents an empty string in S1, so move to the previous character in S1 (i-1, j).
        # 2. '*' represents one or more characters in S1, so move to the previous character in S2 (i, j-1).
        dp[i][j] = wildcardMatchingUtil(S1, S2, i - 1, j, dp) or wildcardMatchingUtil(S1, S2, i, j - 1, dp)
    else:
        dp[i][j] = False  # Characters don't match, and S1[i] is not '*'

    return dp[i][j]

def wildcardMatching(S1, S2):
    n = len(S1)
    m = len(S2)

    # Initialize a 2D DP array with -1 values
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    # Calculate and return the result of wildcard matching
    return wildcardMatchingUtil(S1, S2, n - 1, m - 1, dp)

def main():
    S1 = "ab*cd"
    S2 = "abdefcd"

    if wildcardMatching(S1, S2):
        print("String S1 and S2 do match")
    else:
        print("String S1 and S2 do not match")

if __name__ == "__main__":
    main()

