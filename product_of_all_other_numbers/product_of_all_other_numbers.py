"""
Input: a List of integers
Returns: a List of integers
"""


def product_of_all_other_numbers(arr):
    products = [1 for _ in arr]
    temp = 1

    for i in range(len(arr)):
        products[i] = temp
        temp *= arr[i]

    temp = 1
    for j in range(len(products) - 1, -1, -1):
        products[j] *= temp
        temp *= arr[j]
    return products


if __name__ == "__main__":
    import time

    # Use the main function to test your implementation
    arr = [
        2,
        6,
        9,
        8,
        2,
        2,
        9,
        10,
        7,
        4,
        7,
        1,
        9,
        5,
        9,
        1,
        8,
        1,
        8,
        6,
        2,
        6,
        4,
        8,
        9,
        5,
        4,
        9,
        10,
        3,
        9,
        1,
        9,
        2,
        6,
        8,
        5,
        5,
        4,
        7,
        7,
        5,
        8,
        1,
        6,
        5,
        1,
        7,
        7,
        8,
    ]
    arr = [1, 7, 3, 4]

    start = time.time()

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}"
    )
    print(f"it took: {time.time() - start} seconds.")
