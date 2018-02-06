import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import Prog


def main():
    # ex23_0 = get_input_by_lines(23)
    # ex23 = list(map(lambda x: x.split(), ex23_0))

    # Temporary hardcoded solution
    # Mus take maximum value of b (109900 in my case)
    # and increments it by value of second-to-last instruction
    # up to maximum value of c,
    # and compute the total number of composite values.
    # `1001 - sum(map(pyprimes.isprime, range(109900, 126901, 17)))`
    print(913)

if __name__ == '__main__':
    main()

