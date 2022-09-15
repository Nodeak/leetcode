class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minp = prices[0]
        profit = 0
    
        for p in prices:
            
            if minp > p:
                minp = p
            
            if p - minp > profit:
                profit = p - minp
                
        return profit
        