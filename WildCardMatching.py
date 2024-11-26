
def wildcardMatching(pattern, text):
    #  -------------------------------------RECURSION + MEMOIZATION ----------------------------------------------------------------
    # def isAllStars(S1, i):
    #     # Helper function to check if all characters up to index i in S1 are '*'
    #     for j in range(i + 1):
    #         if S1[j] != '*':
    #             return False
    #     return True

    # def matchChars(i, j, dp):
    #     # Base Cases
    #     if i < 0 and j < 0:  # Both pattern and text are exhausted
    #         return True
    #     if i < 0 and j >= 0:  # Pattern is exhausted but text is not
    #         return False
    #     if i >= 0 and j < 0:  # Text is exhausted but pattern may still have '*'
    #         return isAllStars(pattern, i)
        
    #     # Memoized result
    #     if dp[i][j] != -1:
    #         return dp[i][j]
        
    #     # Matching characters or '?'
    #     if pattern[i] == text[j] or pattern[i] == '?':
    #         dp[i][j] = matchChars(i - 1, j - 1, dp)
    #     # '*' can match zero or more characters
    #     elif pattern[i] == '*':
    #         dp[i][j] = matchChars(i - 1, j, dp) or matchChars(i, j - 1, dp)
    #     else:  # Characters do not match
    #         dp[i][j] = False

    #     return dp[i][j]

    m = len(pattern)
    n = len(text)
    # dp = [[-1 for _ in range(n)] for _ in range(m)]
    # return matchChars(m - 1, n - 1, dp)

# -----------------------------------------------TABULATION: ----------------------------------------------------------------

    # dp = [[False for _ in range(n+1)] for _ in range(m+1)]
    # dp[0][0] = True
    # for j in range(1,n):
    #     dp[0][j] = False
    # for i in range(1,m):
    #     if pattern[i-1] == '*':
    #         dp[i][0] = True
    #     else:
    #         break

    # for i in range (1,m+1):
    #     for j in range(1,n+1):
    #         if pattern[i-1] == text[j-1] or pattern[i-1]== '?':
    #             dp[i][j] = dp[i-1][j-1]
    #         elif pattern[i-1] == '*':
    #             dp[i][j] = dp[i-1][j] or dp[i][j-1]
    #         else:
    #             dp[i][j]= False

    # return dp[m][n]

# -----------------------------------------------SPACE OPTIMIZATION: ----------------------------------------------------------------

    def isAllStars(S1, i):
        for j in range(1, i + 1):
            if S1[j - 1] != '*':
                return False
        return True
    prev = [False for _ in range(n+1)]

    prev[0] = True
    for j in range(1,n):
        prev[j] = False

    for i in range (1,m+1):
        curr = [False for _ in range(n+1)]
        curr[0] = isAllStars(pattern, i)
        for j in range(1,n+1):
            if pattern[i-1] == text[j-1] or pattern[i-1]== '?':
                curr[j] = prev[j-1]
            elif pattern[i-1] == '*':
                curr[j] = prev[j] or curr[j-1]
            else:
                curr[j]= False

        prev = curr
    # print(prev[n])
    return prev[n]

def main():
    S1 = "ab*cd"
    S2 = "abdefcd"

    if wildcardMatching(S1, S2):
        print("String S1 and S2 do match")
    else:
        print("String S1 and S2 do not match")

if __name__ == "__main__":
    main()




def wildcardMatching(pattern, text):

    # def isAllStars(S1, i):
    # # Helper function to check if all characters up to index i in S1 are '*'
    #     for j in range(i + 1):
    #         if S1[j] != '*':
    #             return False
    #     return True

    # def matchChars(i,j,dp):
    #     if i<0 and j<0:
    #         return True
    #     if i<0 and j>=0:
    #         return False
    #     if i>=0 and j<0:
    #         return isAllStars(pattern, i)
    #     if dp[i][j] !=-1:
    #         return dp[i][j]
    #     if pattern[i] == text[j] or pattern[i]== '?':
    #         dp[i][j] = matchChars(i-1,j-1, dp)
    #     elif pattern[i] == '*':
    #         dp[i][j] = matchChars(i-1,j, dp) or matchChars(i,j-1, dp)
    #     else:
    #         dp[i][j]= False

    #     return dp[i][j]

    #m = len(pattern)
    #n = len(text)
    # dp = [[-1 for _ in range(n)] for _ in range(m)]
    # return matchChars(m-1,n-1,dp)

    dp = [[False for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = True
    for j in range(1,n):
        dp[0][j] = False
    for i in range(1,m):
        
    
    

