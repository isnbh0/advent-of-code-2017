import sys
sys.path.append('..')
from get_input import get_input_by_lines

import re
from functions import process, get_weight, where_to_go, find_wrong


def main():
    ex7_0 = get_input_by_lines(7)
    ex7 = process(ex7_0)

    print(get_weight(ex7, where_to_go(ex7, find_wrong(ex7_0)[0])[0]))    

if __name__ == '__main__':
    main()

