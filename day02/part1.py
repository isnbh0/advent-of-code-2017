import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np


def main():
    def listrange(mylist):
        mylist = sorted(mylist)
        return mylist[-1] - mylist[0]

    ex2_0 = get_input_by_lines(2)
    ex2 = np.array([x.split(',') for x in ex2_0]).astype(np.int32)

    print(np.apply_along_axis(listrange, axis=1, arr=ex2).sum())

if __name__ == '__main__':
    main()

