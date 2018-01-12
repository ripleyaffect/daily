"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded
as 'aaa, 'ka', and 'ak'.

"""


def get_encoding_count(sequence, length=None):
    """Return count of possible encodings of `encoding`

    :param encoding: `str` sequence of encoded letters
    :param length: length of sequence. default is None

    """
    if length == None:
        length = len(sequence)

    # Handle base cases
    if length in (0, 1):
        return 1

    count = 0

    if sequence[length - 1] > '0':
        count += get_encoding_count(sequence, length - 1)

    if (
            sequence[length - 2] == '1' or
            (sequence[length - 2] == '1' and sequence[length - 1] < '7')):
        count += get_encoding_count(sequence, length - 2)

    return count


if __name__ == '__main__':
    sequence = '111'
    print(get_encoding_count(sequence))
    sequence = '1226'
    print(get_encoding_count(sequence))
