#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # create an array of length amount + 1
    # each index will represent an amount
    combinations = [0 for _ in range(amount + 1)]
    # for the amount 0, there's only one way to make change
    combinations[0] = 1

    for i in range(len(denominations)):
        current_coin = denominations[i]
        # for each coin in the denominations, we check to see
        # if the current amount i greater or equal to the coin
        # which means we can use the previous combination to get the current one
        for j in range(1, len(combinations)):
            if j >= current_coin:
                combinations[j] += combinations[j - current_coin]
    # now each amount in the array has a combination which is the number of ways
    # to make change for it, and each amount is an index in the array
    # so to get the number of ways for amount, we simpley access the index [amount]
    return combinations[amount]


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

