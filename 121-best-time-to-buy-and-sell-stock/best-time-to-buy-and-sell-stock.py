class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
        '''mini=min(prices)
        i=prices.index(mini)
        for i in range(1,len(prices)):
            if(prices[i]<prices[0]):
                mini=prices[i]
        maxlist=prices[i:len(prices)]
        maxi=max(maxlist)
        profit=maxi-mini
        return profit
        return 0       ''' 
    
              
