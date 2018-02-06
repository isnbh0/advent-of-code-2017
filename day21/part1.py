import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import PixelGrid, INIT_ARR
from functions import dictify


def main():
    ex21_0 = get_input_by_lines(21)
    ex21 = dictify(ex21_0)

    pixelgrid = PixelGrid(key_=ex21, arr_=INIT_ARR)
    pixelgrid.iterate(5)
    print(pixelgrid.get_count())

if __name__ == '__main__':
    main()

