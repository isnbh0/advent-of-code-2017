import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import PixelGrid, INIT_ARR
from functions import dictify


def main():
    print("This code takes about 75s to run. Ctrl+C to break before then.")

    ex21_0 = get_input_by_lines(21)
    ex21 = dictify(ex21_0)

    pixelgrid = PixelGrid(key_=ex21, arr_=INIT_ARR)
    pixelgrid.iterate(18)
    print(pixelgrid.get_count())

if __name__ == '__main__':
    main()

