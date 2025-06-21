"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def maxProfit(prices):
    buy = sell = 0
    max_profit = 0
    for p in range(len(prices)):
        if prices[p] < prices[buy]:
            buy = p
        else:
            sell = p
            max_profit = max(max_profit, prices[sell] - prices[buy])
    return max_profit


def main():
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [2, 4, 1],
        [7, 6, 4, 3, 1]
    ]
    for prices in test_cases:
        print(maxProfit(prices))


if __name__ == '__main__':
    main()
