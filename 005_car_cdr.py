"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first
and last element of that pair. For example, car(cons(3, 4)) returns 3, and
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    return lambda f : f(a, b)

Implement car and cdr.

"""


def cons(a, b):
    """Return a function to delay evaluation with `a` and `b`

    :param a: any value to pass as the first argument to the returned function
    :param b: any value to pass as the second argument to the returned function

    """
    return lambda f : f(a, b)


# Basic implementations of car and cdr
car = lambda f: f(lambda a, b: a)
cdr = lambda f: f(lambda a, b: b)


# Function to generate car and cdr-like functions
def function_index_getter(index):
    """Return a car/cdr-like function that gets the item at `index` from
    a `cons` call, given the above implementation

    :param index: `int` index to get
    """
    return lambda f: f(lambda *attrs: attrs[index])


# generated car and cdr functions
car_2 = function_index_getter(0)
cdr_2 = function_index_getter(1)
cdr_3 = function_index_getter(-1)


if __name__ == '__main__':
    a = 1
    b = 2

    pair = cons(a, b)

    # Test both implementations
    print(car(pair))
    print(cdr(pair))

    print(car_2(pair))
    print(cdr_2(pair))
    print(cdr_3(pair))
