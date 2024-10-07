#!/usr/bin/python3
def makeChange(coins, total):
    # If the total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize a list to store the minimum coins needed for each amount up to total
    # We use total + 1 since we want to include the total amount in our list
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the total 0
    
    # Iterate over each coin
    for coin in coins:
        # Update the dp list for all amounts from coin to total
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still float('inf'), it means we can't make that total with the given coins
    return dp[total] if dp[total] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
total = 11
print(makeChange(coins, total))  # Output: 3 (5 + 5 + 1)

