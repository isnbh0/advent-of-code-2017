import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functools import reduce
import numpy as np
from functions import knot_hash


def main():
    ex10_0 = get_input_by_lines(10)
    ex10 = [int(x) for x in ex10_0[0].split(',')]

    print(knot_hash(ex10))

if __name__ == '__main__':
    main()

