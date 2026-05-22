class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # ################
        # # dp[x] =
        # # number of ways to make amount x
        # dp = [0] * (amount + 1)

        # # Base case:
        # # There is exactly one way
        # # to make amount 0:
        # # choose no coins
        # dp[0] = 1

        # # Process each coin one at a time
        # for coin in coins:

        #     # Update all amounts
        #     # that can include this coin
        #     for current_amount in range(coin, amount + 1):

        #         # Add:
        #         # ways to make the remaining amount
        #         dp[current_amount] += (
        #             dp[current_amount - coin]
        #         )

        # # Final answer
        # return dp[amount]
        # ###################################

        # ###################################
        # cache = {}
        # def dfs (i, a):
        #     if a == amount:
        #         return 1
        #     if a > amount:
        #         return 0
        #     if i == len(coins):
        #         return 0
        #     if (i,a) in cache:
        #         return cache[(i,a)]

        #     cache[(i,a)] = dfs (i, a + coins[i]) + dfs(i+1, a)
        #     return cache[(i,a)]

        # return dfs(0,0)

        # ###################################

        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)-1,-1,-1):
            nextDP = [0] * (amount+1)
            nextDP[0] =1

            for a in range (1,amount +1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a-coins[i]]
            dp = nextDP
        return dp[amount]





















