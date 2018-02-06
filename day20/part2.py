import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import Particle, ParticleSet


def main():
    print("This code takes about 5s to run. Ctrl+C to break before then.")

    ex20_0 = get_input_by_lines(20, strip=False)
    ex20 = list(map(lambda x: x.split(', '), ex20_0)) 

    ps = ParticleSet(infostrs=ex20)

    for i in range(50):
        ps.step(collisions=True)

    print(len(ps.particles))

if __name__ == '__main__':
    main()

