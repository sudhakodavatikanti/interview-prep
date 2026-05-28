class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       max_profit, lowest = 0, prices[0]
       for i in range(1, len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]

        if prices[i] - lowest > max_profit:
            max_profit = max_profit - lowest

        return max_profit


solution = Solution()
prices = [5,1,5,6,7,1,10]
print(solution.maxProfit(prices))