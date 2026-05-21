class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #key = (day,holding)
        memo = {}

        def dfs(day, holding):
            if day >= len(prices):
                return 0
            if (day,holding) in memo:
                return memo[(day,holding)]
            
            cooldown = dfs(day+1,holding)

            #currently own a coin
            if holding:
                #sell coin on the day
                sell = prices[day] + dfs(day +2, False)
                memo[(day,holding)] = max(sell,cooldown)
            #when we dont current own a coin    
            else:
                buy = -prices[day] + dfs(day +1, True)

                memo[(day,holding)] = max(buy,cooldown)

            return memo[(day,holding)]


        return dfs(0,False)