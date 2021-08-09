def getMaxProfit(prices: list) -> int:
    profit = 0
    j = 1

    for i in prices:
        if j < len(prices):
            if i < prices[j]:
                profit += prices[j] - i
        j += 1

    return profit


def main():
    prices = [1, 2, 4]
    print(getMaxProfit(prices))


main()
