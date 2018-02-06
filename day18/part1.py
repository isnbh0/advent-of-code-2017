import sys
sys.path.append('..')
from get_input import get_input_by_lines

from classes import Register


def main():
    ex18_0 = get_input_by_lines(18)
    ex18 = list(map(lambda x: x.split(), ex18_0))

    register = Register(ex18)
    print(register.run())

if __name__ == '__main__':
    main()

