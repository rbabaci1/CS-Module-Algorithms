"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""
from collections import deque


def sliding_window_max(arr, k):
    Q = deque()
    result = []

    for i in range(k):
        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    for i in range(k, len(arr)):
        result.append(arr[Q[0]])
        while Q and Q[0] <= i - k:
            Q.popleft()

        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()
        Q.append(i)
    result.append(arr[Q[0]])
    return result


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
