"""
Given a list of integers, write a function that returns the largest sum
of non-adjacent numbers.

For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

"""

def largest_non_adjacent_sum(ints):
    """Return the largest sum of non-adjacent numbers

    We keep a running sum of "with last value" and "without last value".
    The current value can only be added to the "without last value" total, which
    becomes the next "with last value". The next "without last value" becomes
    the max of the previous two, as the next value is non-adjacent to either.

    :param ints: `list` of `int`s to use

    """
    # Initialize the "with" and "without" last value
    w = 0
    wo = 0

    for val in ints:
        # Whatever is higher, that's your highest possible without `val`
        next_wo = max(w, wo)

        # "Without last" added to val is highest non-adjacent sum
        w = wo + val

        # Set the next "Without last"
        wo = next_wo

    # Return the max of thet two
    return max(w, wo)


if __name__ == '__main__':
    ints = [5, 2, 1, 5]
    print(largest_non_adjacent_sum(ints))
