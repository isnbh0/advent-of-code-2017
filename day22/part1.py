import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import VirusGrid


def main():
    ex22_0 = get_input_by_lines(22)
    ex22 = np.array([list(x) for x in ex22_0]) 

    virusgrid = VirusGrid(ex22)
    for i in range(10000):
        virusgrid.burst()
    print(virusgrid.infect_cnt)

if __name__ == '__main__':
    main()

