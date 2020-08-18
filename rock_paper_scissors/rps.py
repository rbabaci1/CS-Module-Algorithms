#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    possible_plays = ["rock", "paper", "scissors"]
    results = []

    def play(rounds, played=[]):
        if rounds == 0:
            return results.append(played)
        else:
            for i in range(3):
                play(rounds - 1, played + [possible_plays[i]])

    play(n)
    return results


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

