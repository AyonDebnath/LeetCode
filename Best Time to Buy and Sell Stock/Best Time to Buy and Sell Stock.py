class Solution:
    def maxProfit(self, prices: [int]) -> int:
        currMaxSP = float('-inf')
        currMinCP = float('inf')
        currMaxProfit = 0

        buyingIndex = -1
        sellingIndex = -1

        for i in range(len(prices)):
            if prices[i] < currMinCP:
                currMinCP = prices[i]
                buyingIndex = i
                currMaxSP = float('-inf')
            if prices[i] > currMaxSP and i >= buyingIndex:
                currMaxSP = prices[i]
                if currMaxProfit < (currMaxSP - currMinCP):
                    currMaxProfit = currMaxSP - currMinCP
        return currMaxProfit

sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4]))