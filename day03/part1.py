import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np


def main():
    corner_map = {
        0 : ( 1,  1),
        1 : (-1,  1),
        2 : (-1, -1),
        3 : ( 1, -1)
    }

    minus_map = {
        0 : ( 0, -1),
        1 : ( 1,  0),
        2 : ( 0,  1),
        3 : (-1,  0)
    }

    def odd_sqrt(x):
        if x == 1:
            return 0
        n = int((x-1)**0.5)
        return n if n&1 else (n-1)

    def find_corner(x):
        if x == 1:
            return 0, 0
        s = odd_sqrt(x)
        return ((x - s**2 - 1) // (s+1)), odd_sqrt(x)

    def get_coord(x):
        if x == 1:
            return (0, 0)
        corner_type, start_sq = find_corner(x)
        upper_right = ((start_sq+1)/2, (start_sq+1)/2)
        
        coord = np.array(upper_right) * np.array(corner_map[corner_type])
        coord += (start_sq**2 + (corner_type+1)*(start_sq+1) - x)\
                *(np.array(minus_map[corner_type]))
        return tuple([int(x) for x in coord])

    def manhattan(x):
        return sum([abs(c) for c in get_coord(x)])

    ex3 = int(get_input_by_lines(3)[0])

    print(manhattan(ex3))

if __name__ == '__main__':
    main()

