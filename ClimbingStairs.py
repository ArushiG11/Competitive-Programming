class Solution:
    def climbStairs(self, n):
        # Recursion as we need to find number of ways (Top Down)
        # if (n==0 or n==1): 
        #     return 1 
        #here since we already came down to 0th
        #when we are at 1st step we can have only one way, that is taking one step
        # fs = self.climbStairs(n-1)
        # ss = self.climbStairs(n-2)
        # return fs+ss

        # We could have used memoization by passing the dp array to store the values of both function. That will reduce TC to O(n)

# Tabulation - Bottom up
        # dp = [-1]*(n+1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i] = dp[i-1]+dp[i-2]

        # return dp[n]

# Space Optimization

        prev2 = 1
        prev = 1
        for i in range(2,n+1):
            curr = prev+prev2
            prev2 = prev
            prev = curr

        return prev
        
def main():
    solution = Solution()
    
    print("Climbing Stairs Problem Solver")
    print("============================")
    print("This program calculates the number of distinct ways to climb n stairs,")
    print("taking either 1 or 2 steps at a time.")
    
    n = int(input("\nEnter the number of stairs: "))
    result = solution.climbStairs(n)
    print(f"\nNumber of distinct ways to climb {n} stairs: {result}")
    
if __name__=="__main__":
    main()
    

        