"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""
from collections import deque


def sliding_window_max(arr, k):
    # Create a deque to store k elements.
    Q = deque()
    result = []

    # Run a loop and insert first k elements in the deque. While inserting the element if the element at the back of the queue is smaller than the current element remove all those elements and then insert the element.
    for i in range(k):
        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    # Now, run a loop from k to end of the array.
    for i in range(k, len(arr)):
        result.append(arr[Q[0]])
        # Remove the element from the front of the queue if they are out of the current window.
        while Q and Q[0] <= i - k:
            Q.popleft()

        # Insert the next element in the deque. While inserting the element if the element at the back of the queue is smaller than the current element remove all those elements and then insert the element.
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
