import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np


def main():
    ex6_0 = get_input_by_lines(6)
    ex6 = [int(x) for x in ex6_0[0].split(',')]

    seen = []
    current = ex6
    count = 0
    
    while (current not in seen) and (count <= 2000000):
        seen.append(current.copy())
        idx = np.argmax(current)
        maxval = current[idx]
        current[idx] = 0

        while maxval > 0:
            idx = (idx + 1) % len(current)
            current[idx] += 1
            maxval -= 1
        
        count += 1
    
    print(count)

if __name__ == '__main__':
    main()

