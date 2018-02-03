import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from functools import reduce


def main():
    print("This code takes about 15s to run. Ctrl+C to break before then.")

    ex17_0 = get_input_by_lines(17)
    ex17 = int(ex17_0[0])

    count = 0
    idx = 0
    recent = 0

    while count <= 50e6:
        if count >= 1:
            idx = (idx + ex17) % (count + 1) + 1
        else:
            idx = 1

        if idx == 1:
            recent = count+1
        count += 1

    print(recent)

if __name__ == '__main__':
    main()

