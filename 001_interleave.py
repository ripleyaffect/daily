"""
Given a stack of N elements, interleave the first half of the stack with the
second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue
from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become
[1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become
[1, 4, 2, 3].

"""

# Try importing from Python 3
try:
    from queue import Queue
except ImportError:
    from Queue import Queue


def interleave(stack):
    """Return the interleaved `stack`

    Interleave the first half of `stack` with the reversed second half

    :param stack: `list` of items to interleave

    """
    # Create an empty queue
    queue = Queue()

    # Handle the empty stack case
    if not stack:
        return stack

    # Initialize vars, take the first item off the stack
    temp = stack.pop()
    count = 0

    # Find out how tall the stack is
    while stack:
        queue.put(temp)
        temp = stack.pop()
        count += 1

    # Add back one item
    stack.append(temp)

    # Loop until interleaving is completed
    while count:
        # Reverse all items onto the stack
        for _ in xrange(count):
            stack.append(queue.get())

        # Reduce the count
        count -= 1

        # Push `count` items back into the queue
        for _ in xrange(count):
            queue.put(stack.pop())

    return stack


if __name__ == '__main__':
    stack = [1, 2, 3, 4, 5]
    print(interleave(stack))
