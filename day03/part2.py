import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import SpiralGrid

def main():
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

