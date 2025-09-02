class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            current_price = prices[i]

            if current_price < buy:
                buy = current_price

            elif (current_price - buy) > profit:
                profit = current_price - buy
        return profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))

# it is the Kadane's Algorithm. the time complexity of this problem is O(n) and space complexity of this problem is O(1) 


# previous O(n^2) solution

class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            if (max(prices[i+1:]) - prices[i]) >profit:
                profit = max(prices[i:]) - prices[i]
        return profit
    
# it is n^2 for because the loop is O(n) and for the max and slicing is O(n+m). The space complexity will be O(n), as slicing the list multiple time will consume space.