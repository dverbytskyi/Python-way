import unittest
import math

"""
    Develop a function that will take, start range, end range, and some input number
    It should return a list of numbers that contains an input number.
    Don't use string methods
    Example:
        find_number(1, 5, 25) will return [5, 15, 25]
"""

def check_number(item, to_check):
    if item > 0:
        max_power = int(math.log10(item)) + 1
    elif item == 0:
        max_power = 1
    else:
        max_power = int(math.log10(-item)) + 2

    # max_power = math.ceil(math.log10(item)) + 1

    while item > 0:
        for numb in range(0, max_power):
            part, remainder = divmod(item, 10**numb)  
            if part == to_check or remainder == to_check:
                return True
        item //= 10

    return False


def find_numbers(start, number, end):
    list_numbers = [item for item in range(start, end+1) if check_number(item, number)]

    return list_numbers


class Test(unittest.TestCase):
    def test_positive_find_numbers(self):
        assert find_numbers(0, 1, 150) == [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 31, 41, 51, 61, 71, 81, 91, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
        assert find_numbers(10, 9, 150) == [19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 109, 119, 129, 139, 149]
        assert find_numbers(5, 5, 150) == [5, 15, 25, 35, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 65, 75, 85, 95, 105, 115, 125, 135, 145, 150]
        assert find_numbers(5, 5, 35) == [5, 15, 25, 35]


if __name__ == '__main__':
    unittest.main()
