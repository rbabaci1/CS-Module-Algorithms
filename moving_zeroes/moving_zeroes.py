"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # iterate over the array
    # if 0 is found, shift all numbers to the left
    # move the 0 to the end of the array
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            j = i
            while j < len(arr) - 1:
                arr[j] = arr[j + 1]
                j += 1
            arr[j] = 0
    return arr


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
