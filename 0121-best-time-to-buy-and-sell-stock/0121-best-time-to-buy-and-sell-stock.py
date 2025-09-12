import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxp = 0
        n= len(prices)
        for i in range(1,n):
            if buy> prices[i]:
                buy = prices[i]
            else:
                maxp =max(maxp,(prices[i]-buy))
        return maxp        