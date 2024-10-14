#!/usr/bin/python3
"""0-making change module
"""


def makeChange(coins, total):
    """ make change function
    """
    # if total is less than 1 no coins are needed
    if total <= 0:
        return 0

    table = [float('inf')] * (total + 1)
    table[0] = 0

    # fill the table
    for coin in coins:
        for i in range(coin, total + 1):
            table[i] = min(table[i], table[i - coin] + 1)

    return table[total] if table[total] != float('inf') else -1
