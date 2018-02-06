import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np
from classes import TM
from functions import encode_instr


NUM_STEPS = 12261543

def main():
    print("This code takes about 7s to run. Ctrl+C to break before then.")

    ex25_0 = get_input_by_lines(25)
    ex25 = encode_instr(ex25_0)

    tm25 = TM(ex25)
    tm25.step(NUM_STEPS)
    print(tm25.checksum())

if __name__ == '__main__':
    main()

