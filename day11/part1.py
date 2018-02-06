import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import simplify_coords, make_coords


def main():
    ex11_0 = get_input_by_lines(11)
    ex11 = ex11_0[0].split(',')

    print(simplify_coords(*make_coords(ex11)[:3]))

if __name__ == '__main__':
    main()

