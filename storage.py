# encoding=utf-8

from binascii import hexlify
from itertools import izip_longest, chain
import re
from pprint import pprint

from prettytable import PrettyTable


def tobin(x, count=16):
    _ret = "".join(map(lambda y: str((x >> y) & 1), range(count - 1, -1, -1)))
    return " ".join(re.findall(r'[01]{4}', _ret))


def store_program(data):
    _ret = []
    lines = [d.strip() for d in data.strip().splitlines()]
    _out = {
        line: [hexlify(d) for d in line] for line in lines
    }

    for key in lines:
        _out[key] += ['0D']

        l = _out[key]
        for a, b in izip_longest(l[::2], l[1::2]):
            to_add = [tobin(int(s, 16), 4) for i, s in enumerate(a + (b if b else ''))]
            _ret.append(to_add)

    return _ret


def show_store_program(data):

    table = store_program(data)
    return [" ".join(d) for d in table]


def show_bin_rep(data):

    table = PrettyTable(['Binary Representation'])
    bins = list(chain.from_iterable(store_program(data)))
    for i in range(0, len(bins), 4):
        table.add_row([bins[i] + bins[i+1] + bins[i + 2] + bins[i + 3]])
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
    # program = 'ORG 0'
    # data = store_program(program)

    # pprint(data)
    # pprint(show_store_program(program))
    print show_bin_rep(program)
    pprint(store_program(program))