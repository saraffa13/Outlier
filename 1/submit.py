def can_empty_piles(a, b):
    # Create a 2D DP table with dimensions (a+1) x (b+1)
    dp = [[False] * (b + 1) for _ in range(a + 1)]
    
    # Base case: if both piles are empty
    dp[0][0] = True
    
    # Fill the DP table
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i >= 1 and j >= 2:
                dp[i][j] = dp[i - 1][j - 2] or dp[i][j]
            if i >= 2 and j >= 1:
                dp[i][j] = dp[i - 2][j - 1] or dp[i][j]
    
    # The result is whether we can empty the given piles
    return dp[a][b]

def solve_test_cases():
    t = int(input())  # Number of test cases
    for _ in range(t):
        a, b = map(int, input().split())
        if can_empty_piles(a, b):
            print("YES")
        else:
            print("NO")

# Call the function to handle test cases
solve_test_cases()