class Solution:
    def maxProfit(self, prices: [int]) -> int:
        currCP = prices[0]
        currSP = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] >= currCP:
                if maxProfit < prices[i] - currCP:
                    maxProfit = prices[i] - currCP
                    currSP = prices[i]
            else:
                currCP = prices[i]
                currSP = prices[i]
        return maxProfit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))