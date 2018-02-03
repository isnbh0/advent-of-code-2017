import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np

def main():
    def init_stack(ex13):
        dict0 = dict()
        for line in ex13:
            idx, range_ = line.split(': ')
            idx, range_ = int(idx), int(range_)
            dict0[idx] = {'pos': 0, 'dir_': 'd',
                          'range_': range_}
        return dict0    

    ex13_0 = get_input_by_lines(13)
    ex13 = init_stack(ex13_0)

    ex13_new = [(x, 2*ex13[x]['range_']-2) for x in ex13.keys()]

    # Currently hardcoded because starting at 1 takes too long
    # TODO: implement with Chinese Remainder Theorem
    for i in range(3890000, 20000000):
        rr = np.array(ex13_new)[:, 0] + i
        if (rr % np.array(ex13_new)[:, 1]).min() > 0:
            print(i)
            break

if __name__ == '__main__':
    main()

