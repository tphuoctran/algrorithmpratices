'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
##Brute Force Approach O(n^2) time complexity and O(1) space complexity
# def maxProfit(self, prices: list[int]) -> int:
#     max = 0

#     for i in range(len(prices)):
#         j = i + 1
#         while j < len(prices):
#             if max < prices[j] - prices[i]:
#                 max = prices[j] - prices[i]
#             j += 1
#     return max

###Optimized Approach O(n) time complexity and O(1) space complexity
##first loop through the array to find the lowest price index and max value for the profit for that 
## then loop through the rest of the array to find the max profit
def maxProfit(self, prices: list[int]) -> int:
    lowestPriceIndx = 0
    max = 0

    for i in range(len(prices)):
        if prices[i] < prices[lowestPriceIndx]:
            lowestPriceIndx = i
        if max < prices[i] - prices[lowestPriceIndx]:
            max = prices[i] - prices[lowestPriceIndx]

    j = lowestPriceIndx + 1
    while j < len(prices):

        if max < prices[j] - prices[lowestPriceIndx]:
            max = prices[j] - prices[lowestPriceIndx]
        j += 1
        
    return max


prices = [1,2]
print("Input: prices = ", prices)
print("Output: ", maxProfit(0, prices))