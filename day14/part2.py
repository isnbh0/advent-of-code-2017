import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import count_regions


def main():
    ex14_0 = get_input_by_lines(14)
    ex14 = ex14_0[0]

    print(count_regions(ex14))

if __name__ == '__main__':
    main()

