"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""


def sliding_window_max(numbers, k):
    # loop over the numbers till len(numbers) - k to avoid accessing out of range
    # pick the max number in that size window
    result = []
    for i in range(len(numbers) - k + 1):
        j = i
        max_value = numbers[j]

        while j < k + i:
            if numbers[j] > max_value:
                max_value = numbers[j]
            j += 1
        result.append(max_value)
    return result


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
