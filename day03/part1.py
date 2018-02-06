import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import corner_map, minus_map, odd_sqrt,\
                      find_corner, get_coord, manhattan


def main():
    ex3 = int(get_input_by_lines(3)[0])

    print(manhattan(ex3))

if __name__ == '__main__':
    main()

