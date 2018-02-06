import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import score_group


def main():
    ex9_0 = get_input_by_lines(9)
    ex9 = ex9_0[0]

    print(score_group(ex9)[0])

if __name__ == '__main__':
    main()

