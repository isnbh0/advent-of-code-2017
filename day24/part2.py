import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from functions import make_bridges


def main():
    print("This code takes about 6min to run. Ctrl+C to break before then.")

    ex24_0 = get_input_by_lines(24)
    ex24 = [tuple(map(int, x.split('/'))) for x in ex24_0]

    bridges24 = make_bridges(ex24)

    len24 = [len(x) for x in bridges24]
    max_length = max(len24)

    long24 = [x for x in bridges24 if len(x) == max_length]
    print(max([np.array(x).flatten().sum() for x in long24]))

if __name__ == '__main__':
    main()

