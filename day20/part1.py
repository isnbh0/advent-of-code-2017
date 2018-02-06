import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import ParticleSet

def main():

    ex20_0 = get_input_by_lines(20, strip=False)
    ex20 = list(map(lambda x: x.split(', '), ex20_0)) 

    ps = ParticleSet(infostrs=ex20)
    print(list(map(lambda p: np.abs(p.acc).sum(), ps.particles)).index(1))

if __name__ == '__main__':
    main()

