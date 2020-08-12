#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ["rock", "paper", "scissors"]
    result = []

    if n == 0:
        return [[]]
    elif n == 1:
        return [["rock"], ["paper"], ["scissors"]]
    else:
        # the length of the result will be always 3^n
        # each sub array will always have length of n
        for i in range(pow(3, n)):
            sub = []
            for j in range(n):
                pass

    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

