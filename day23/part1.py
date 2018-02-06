import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import Prog


def main():
    ex23_0 = get_input_by_lines(23)
    ex23 = list(map(lambda x: x.split(), ex23_0))

    p = Prog(ex23)
    print(p.run())

if __name__ == '__main__':
    main()

