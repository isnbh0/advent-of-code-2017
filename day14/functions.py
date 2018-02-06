from functools import reduce
import numpy as np


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

def knot_hash(numlist, str0):
    return run_hash(run_64(baselist, asciify(str0)))

def hash_row(baselist, str0):
    return '{:0>128}'.format(str(bin(int(knot_hash(baselist, str0), 16)))[2:])

def fill_region(row, col, regions, ndgrid, region_count):
    ROWS, COLS = regions.shape
    up = (max(0, row-1), col)
    down = (min(ROWS-1, row+1), col)
    left = (row, max(0, col-1))
    right = (row, min(COLS-1, col+1))

    regions[row, col] = region_count
    filled_any = False

    for neighbor in [right, down, left, up]:
        if neighbor != (row, col) and ndgrid[neighbor] != 0\
        and regions[neighbor] == 0:
            fill_region(*neighbor, regions, ndgrid, region_count)
            filled_any = True
        else:
            pass
    return regions

def count_regions(base_str):
    used = 0 
    grid = []

    for i in range(128):
        grid.extend(int(x) for x in hash_row(baselist, '{0}-{1}'.format(base_str, i)))

    ndgrid = np.array(grid).reshape(128, 128)
    ROWS, COLS = ndgrid.shape
    region_count = 0 
    regions = np.zeros((ROWS, COLS))

    for row in range(ROWS):
        for col in range(COLS):
            if ndgrid[row, col] == 1:
                up = (max(0, row-1), col)
                down = (min(ROWS-1, row+1), col)
                left = (row, max(0, col-1))
                right = (row, min(COLS-1, col+1))

                if regions[row, col] != 0:
                    pass
                else:
                    region_count += 1
                    regions = fill_region(row, col, regions, ndgrid, region_count)
            else:
                continue
    return region_count

