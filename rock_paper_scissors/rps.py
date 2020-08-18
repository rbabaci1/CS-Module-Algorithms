#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = ["rock", "paper", "scissors"]
    # possible_plays = [["rock"], ["paper"], ["scissors"]]
    possible_plays = [
        ["rock", "rock"],
        ["rock", "paper"],
        ["rock", "scissors"],
        ["paper", "rock"],
        ["paper", "paper"],
        ["paper", "scissors"],
        ["scissors", "rock"],
        ["scissors", "paper"],
        ["scissors", "scissors"],
    ]
    result = []


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

