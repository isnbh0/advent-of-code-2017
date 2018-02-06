import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import dictify, get_nbrs


def main():
    ex12_0 = get_input_by_lines(12)
    ex12 = dictify(ex12_0)

    print(len(get_nbrs(ex12, 0, [])))

if __name__ == '__main__':
    main()

