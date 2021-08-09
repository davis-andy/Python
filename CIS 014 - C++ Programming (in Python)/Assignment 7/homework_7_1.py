def getMaxProfit(prices: list) -> int:
    profit = 0
    i = len(prices) - 1
    j = i

    while i >= 0:
        while j >= 0:
            temp = prices[i] - prices[j]
            if temp > profit:
                profit = temp
            j -= 1
        i -= 1
        j = i

    return profit


def main():
    prices = [1, 2, 4]
    print(getMaxProfit(prices))


main()
