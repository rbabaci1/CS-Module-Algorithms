import unittest
import random
from single_number import single_number
import time


class Test(unittest.TestCase):
    def test_single_number(self):
        arr = []

        for i in range(1000):
            arr.append(i)
            arr.append(i)

        random.shuffle(arr)
        rand_index = random.randint(0, len(arr))
        num = arr.pop(rand_index)

        start = time.time()

        self.assertEqual(single_number(arr), num)
        print(f"it took: {time.time() - start} seconds.")


if __name__ == "__main__":
    unittest.main()
