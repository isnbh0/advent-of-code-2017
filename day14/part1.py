import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from functools import reduce


def main():
    baselist = np.arange(256)

    ex14_0 = get_input_by_lines(14)
    ex14 = ex14_0[0]

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
        list0.extend([17, 31, 73, 47, 23])
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
        base16 = baselist.reshape([-1, 16])
        xor_arr = np.apply_along_axis((lambda x: reduce(np.bitwise_xor, x)), axis=1, arr=base16)
        return ''.join([hex(x)[2:].rjust(2, '0') for x in xor_arr])

    def knot_hash(baselist, str0):
        return run_hash(run_64(baselist, asciify(str0)))

    def hash_row(baselist, str0):
        return '{:0>128}'.format(str(bin(int(knot_hash(baselist, str0), 16)))[2:])

    used = 0
    base_str = ex14

    for i in range(128):
        used += ((np.array(list(hash_row(baselist, '{0}-{1}'.format(base_str, i)))).astype(np.int32))==1).sum()
        
    print(used)

if __name__ == '__main__':
    main()

