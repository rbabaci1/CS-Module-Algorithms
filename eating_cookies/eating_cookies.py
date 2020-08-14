"""
Input: an integer
Returns: an integer
"""
import time


def eating_cookies(n):
    # Brute force solution
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

    # Memoization Bottom - Up approach
    # if n == 0 or n == 1:
    #     return 1
    # if n == 2:
    #     return 2

    # result = [0 for _ in range(n + 1)]
    # result[0], result[1], result[2] = 1, 1, 2

    # for i in range(3, n + 1):
    #     result[i] = result[i - 1] + result[i - 2] + result[i - 3]
    # return result[-1]

    # Memoization Top - Down approach
    # def memo_cookies(n, cache={}):
    #     if n == 0 or n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     else:
    #         if n not in cache:
    #             cache[n] = (
    #                 memo_cookies(n - 1) + memo_cookies(n - 2) + memo_cookies(n - 3)
    #             )
    #         return cache[n]

    # return memo_cookies(n)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    start = time.time()
    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
    print(f"it took: {time.time() - start} seconds.")
