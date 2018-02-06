import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import init_stack, get_severity

def main():
    ex13_0 = get_input_by_lines(13)
    ex13 = init_stack(ex13_0)

    print(get_severity(ex13))

if __name__ == '__main__':
    main()

