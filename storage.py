# encoding=utf-8

from binascii import hexlify
import re
import collections
from itertools import islice
from pprint import pprint

from prettytable import PrettyTable

def consume(iterator, n):
    """Advance the iterator n-steps ahead. If n is none, consume entirely."""
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)


def tobin(x, count=16):
    _ret = "".join(map(lambda y: str((x >> y) & 1), range(count - 1, -1, -1)))
    return " ".join(re.findall(r'[01]{4}', _ret))


def store_program(data):
    _ret = []
    lines = [d.strip() for d in data.strip().splitlines()]
    _out = {
        line: [hexlify(d) for d in line] for line in lines
    }

    for key in _out:
        _out[key] += ['0D']

        l = _out[key]
        for a, b in zip(l, l[1:]):
            to_add = [tobin(int(s, 16), 4) for i, s in enumerate(a + b)]
            _ret.append(to_add)

    return _ret


def show_store_program(data):

    table = store_program(data)
    return [" ".join(d) for d in table]


def show_bin_rep(data):

    table = PrettyTable(['Binary Representation'])
    for val in show_store_program(data):
        table.add_row([val])
    return table.get_string()

if __name__ == '__main__':
    program = """
         ORG 0
         LDA A
         ADD B
         STA C
         HLT
    A,   DEC 83
    B,   DEC -23
    C,   HEX 0
         END
    """
    # data = store_program(program)

    # pprint(data)
    pprint(show_store_program(program))