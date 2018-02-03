import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functools import reduce
import numpy as np


def main():
    ex10_0 = get_input_by_lines(10)
    ex10 = [int(x) for x in ex10_0[0].split(',')]

    TAIL = [17, 31, 73, 47, 23]
    baselist = list(range(256))

    def reverse_list(list0, start_idx, rev_len):
        list1 = list0.copy()
        end_idx = start_idx + rev_len - 1
        
        for idx in range(rev_len):
            idx1 = (end_idx - idx) % len(list0)
            idx0 = (start_idx + idx) % len(list0)
            list1[idx1] = list0[idx0]
        return list1

    def asciify(str0):
        list0 = [ord(x) for x in str0] 
        list0.extend(TAIL)
        return list0

    def run_64(baselist, idces):
        curr_idx = 0
        skip_size = 0
        mylist = baselist.copy()

        for i in range(64):
            for val in idces:
                mylist = reverse_list(mylist, curr_idx, val)
                curr_idx += (val + skip_size)
                skip_size += 1
        return mylist

    def run_hash(baselist):
        base16 = np.array(baselist).reshape([-1, 16])
        xor_arr = np.apply_along_axis((lambda x: reduce(np.bitwise_xor, x)), axis=1, arr=base16)
        return ''.join([hex(x)[2:].rjust(2, '0') for x in xor_arr])


    ascii10 = ','.join([str(x) for x in ex10])
    print(run_hash(run_64(baselist, asciify(ascii10))))

if __name__ == '__main__':
    main()

