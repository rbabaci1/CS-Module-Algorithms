"""
Input: a List of integers
Returns: a List of integers
"""


def product_of_all_other_numbers(arr):
    # loop over the array starting from index 0 always
    # computing the product of all the values excluding the one
    # at the current index, then append the result to the products array
    products = []
    for i in range(len(arr)):
        result = 1
        for j in range(len(arr)):
            if j != i:
                result *= arr[j]
        products.append(result)
    return products


if __name__ == "__main__":
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
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

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}"
    )

