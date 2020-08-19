#!/usr/bin/python

import sys


def making_change(amount, denominations):
    combinations = [0 for _ in range(amount + 1)]
    combinations[0] = 1

    for i in range(len(denominations)):
        current_coin = denominations[i]
        for j in range(1, len(combinations)):
            if j >= current_coin:
                combinations[j] += combinations[j - current_coin]
    return combinations[-1]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations), amount=amount
            )
        )
    else:
        print("Usage: making_change.py [amount]")

