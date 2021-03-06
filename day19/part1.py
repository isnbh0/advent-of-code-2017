import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import Map


def main():
    ex19_0 = get_input_by_lines(19, strip=False)
    ex19 = np.array(list(map(list, ex19_0)))

    map19 = Map(ex19)
    map19.set_pos(map19.find_start())

    finished = False
    while not finished:
        finished = map19.step()

    print(''.join(map19.letters))

if __name__ == '__main__':
    main()

