class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #key = (day, Bool-buying power) if bool buying power = True that means we are hold a coin, where were can buy / do nothing, else we dont have a coin, what means we can either sell or do nothing
        memo = {}

        def dfs (day, buying_power):
            if day >= len(prices):
                return 0
            if (day, buying_power) in memo:
                return memo[day,buying_power]

            do_nothing = dfs(day+1,buying_power)

            if buying_power:
                buy = -prices[day] + dfs(day+1,False)
                memo[day,buying_power] = max(buy, do_nothing)
            else:
                sell = prices[day] + dfs(day+2,True)
                memo[day,buying_power] = max(sell, do_nothing)
            
            return memo[day,buying_power]

        return dfs(0,True)