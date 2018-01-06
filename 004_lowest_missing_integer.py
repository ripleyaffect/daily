"""
Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates
and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.

You can modify the input array in-place.
"""


def lowest_missing_integer(array):
    """Return the lowest missing integer from the array

    We use the indexes to keep track of potential candidates, indicating
    whether they're in the array by flipping the sign. To avoid negative
    numbers, any negative numbers are moved to the end of the array and not
    touched after that.

    This works because the lowest missing postive integer cannot be larger
    than the count of positive integers in the array + 1

    Runtime is O(3n) == O(n)

    :param array: `list` of `ints` to fine lowest missing integer for

    """
    count = len(array)
    negative_count = 0

    # move any negative numbers to the end of the array
    for i in xrange(count):
        val = array[i]
        swap_index = count - negative_count - 1
        if val < 1 and swap_index > i:
            array[i] = array[swap_index]
            array[swap_index] = val
            negative_count += 1

    positive_count = count - negative_count

    # Flip the numbers at the index of any numbers in the positives
    for i in xrange(positive_count):
        val = abs(array[i])
        if val <= positive_count:
            array[val - 1] = -array[val - 1]

    # Find and return the first candidate based on the first positive number
    candidate = 1
    for i in xrange(positive_count):
        if array[i] >= 0:
            return candidate
        candidate += 1

    return candidate


if __name__ == '__main__':
    print(lowest_missing_integer([3, 4, -1, 1]))  # 2
    print(lowest_missing_integer([1, 2, 0]))  # 3
    print(lowest_missing_integer([6, 8, 1, 2, 3, 7, -2, 0, 4, 5]))  # 9
    print(lowest_missing_integer([]))  # 1
