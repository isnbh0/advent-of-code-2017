import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from functools import reduce
from functions import hash_row


def main():
    baselist = np.arange(256)

    ex14_0 = get_input_by_lines(14)
    ex14 = ex14_0[0]

    used = 0

    for i in range(128):
        used += ((np.array(list(hash_row(baselist, '{0}-{1}'.format(ex14, i)))).astype(np.int32))==1).sum()
        
    print(used)

if __name__ == '__main__':
    main()

