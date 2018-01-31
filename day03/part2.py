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


    class SpiralGrid():
        def __init__(self, rule_func):
            self.grid = dict()
            self.rule = rule_func
            self.grid[(0, 0)] = 1
            return
        
        def step(self):
            grid_size = len(self.grid)
            new_coord = get_coord(grid_size+1)
            
            self.grid[new_coord]\
            = self.rule(self.grid, new_coord)
            
            return self.grid[new_coord]

    def rule(grid, new_coord):
        new_coord = np.array(new_coord)
        total = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                try:
                    total += grid[tuple(new_coord + np.array((i, j)))]
                except:
                    pass
        return total


    def part2(input_, rule):
        grid = SpiralGrid(rule)
        x = 0
        while x <= input_:
            x = grid.step()
        return x


    ex3 = int(get_input_by_lines(3)[0])

    print(part2(ex3, rule))

if __name__ == '__main__':
    main()

