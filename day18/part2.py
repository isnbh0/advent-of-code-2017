import sys
sys.path.append('..')
from get_input import get_input_by_lines

from classes import Prog, ProgPair


def main():
    ex18_0 = get_input_by_lines(18)
    ex18 = list(map(lambda x: x.split(), ex18_0))

    pair = ProgPair(ex18)
    print(pair.run()[2])

if __name__ == '__main__':
    main()

