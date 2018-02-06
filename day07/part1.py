import sys
sys.path.append('..')
from get_input import get_input_by_lines

import re
from functions import dictify


def main():
    ex7_0 = get_input_by_lines(7)
    ex7 = [dictify(x) for x in ex7_0]

    result = []
    for item in ex7:
        if item['children']:
            result.extend(item['children'])

    print((set(x['name'] for x in ex7) - set(result)).pop())


if __name__ == '__main__':
    main()

