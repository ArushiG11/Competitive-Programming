def findWays(arr, k):
    # Set the modulus value to prevent overflow of large numbers
    mod = 10**9 + 7
    
    # Length of the input array
    n = len(arr)
    
    # Initialize two lists to store ways to achieve each sum up to k
    curr = prev = [0] * (k + 1)
    
    # There's always one way to achieve sum 0, by choosing an empty subset
    prev[0] = 1  
    
    # Special handling for the first element in the array
    if arr[0] == 0:
        # If the first element is 0, then we have two ways to achieve sum 0 (include or exclude this 0)
        prev[0] = 2  
    elif arr[0] <= k:
        # If the first element is within the target range, mark it as achievable by itself
        prev[arr[0]] = 1

    # Iterate over the remaining elements in arr
    for i in range(1, n):
        # Reset curr array for the next iteration
        curr = [0] * (k + 1)
        
        # There's always one way to achieve sum 0: by choosing an empty subset
        curr[0] = 1
        
        # Calculate the number of ways to achieve each sum from 0 up to k using arr[0] to arr[i]
        for j in range(0, k + 1):
            # Ways to achieve sum j without including arr[i]
            no_pick = prev[j]
            
            # Ways to achieve sum j by including arr[i], only if arr[i] is <= j
            pick = prev[j - arr[i]] if arr[i] <= j else 0
            
            # Total ways to achieve sum j: either include or exclude arr[i]
            curr[j] = (pick + no_pick) % mod

        # Move the current row to the previous row for the next iteration
        prev = curr

    # The answer is the number of ways to achieve the target sum k
    return prev[k] % mod


def main():
    arr = [1, 2, 2, 3]
    k = 3
    
    # Find and print the number of subsets that can be formed with a sum of 'k'.
    print("The number of subsets found are", findWays(arr, k))

if __name__ == "__main__":
    main()
