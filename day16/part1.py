import sys
sys.path.append('..')
from get_input import get_input_by_lines

from classes import Danceline


def main():
    ex16_0 = get_input_by_lines(16)
    ex16 = ex16_0[0].split(',')

    starting = 'abcdefghijklmnop'
    line = Danceline(starting)
    print(''.join(line.acts(ex16)))

if __name__ == '__main__':
    main()

