# encoding=utf-8

from itertools import chain
from binascii import unhexlify


def no_spaces(d):
    return [l.split() for l in d]


def bin_to_hex(s):
    _var = hex(int(s, 2))
    return _var[2:]


def convert(bin_list):
    l = list(chain.from_iterable(no_spaces(bin_list)))
    return [unhexlify(bin_to_hex(a) + bin_to_hex(b)) for a, b in zip(l[::2], l[1::2])]


def print_conversion(char_list):
    return "".join([c if c != '\r' else '\n' for c in char_list])


if __name__ == '__main__':
    from storage import show_store_program
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
    conversion = convert(show_store_program(program))
    print print_conversion(conversion)