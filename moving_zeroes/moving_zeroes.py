"""
Input: a List of integers
Returns: a List of integers
"""


def moving_zeroes(arr):
    # iterate over the array and keep a pointer to the
    # location to insert a none zero value
    # move all the none zero values to the beginning of the array
    # when done, replace all the rest starting at the pointer location with 0's

    update_at = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[update_at] = arr[i]
            update_at += 1
    for j in range(update_at, len(arr)):
        arr[j] = 0
    return arr


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
