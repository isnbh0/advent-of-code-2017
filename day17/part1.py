import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from functools import reduce


def main():
    ex17_0 = get_input_by_lines(17)
    ex17 = int(ex17_0[0])

    count = 0
    idx = 0
    mylist = []

    while count <= 2017:
        if mylist:
            idx = (idx + ex17) % len(mylist) + 1
        mylist.insert(idx, count)
        count += 1

    idx0 = mylist.index(2017)
    print(mylist[idx0+1])

if __name__ == '__main__':
    main()

