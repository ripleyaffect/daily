"""
Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the
original array except the one at i. Solve it without using division
and in O(n) time.

For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the
expected output would be [2, 3, 6].
"""

def get_product_except_list(ints):
    """Return the list with the above requirements

    A list of products going forward and a list of products going backward are
    combined to create a list of products excluding the number at the current
    index.

    Runtime is O(5n) => O(n).

    :param ints: `list` of `ints` to turn into a "product exept" `list`

    """
    # Handle case of empty list
    if not ints:
        return ints

    # Create a list of products going forward
    product = 1
    products_forward = []
    for i in ints:
        product *= i
        products_forward.append(product)

    # Create a list of products going backwards
    product = 1
    products_backward = []
    for i in ints[::-1]:
        product *= i
        products_backward.append(product)

    # Reverse the products_backward
    products_backward.reverse()

    # Buffer product lists to make the logic simpler
    products_forward = [1] + products_forward
    products_backward = products_backward + [1]

    # Combine the product lists, excluding the current index
    return [
        products_forward[i] * products_backward[i + 1]
        for i in xrange(len(ints))]


if __name__ == '__main__':
    ints = [1, 2, 3, 4, 5]
    print(get_product_except_list(ints))
