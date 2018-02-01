import sys
sys.path.append('..')
from get_input import get_input_by_lines

import re


def main():
    ex7_0 = get_input_by_lines(7)
    ex7 = ex7_0 

    def dictify(lines):
        name = re.search(r'\w+', lines).group(0)
        weight = int(re.search(r'\((\d+)\)', lines).group(1))
        children = re.search(r'-\> (.+)$', lines)
        if children:
            children = children.group(1).split(', ')
        return {'name': name, 'weight' : weight, 'children' : children}

    input_dict = [dictify(x) for x in ex7]

    result = []
    for item in input_dict:
        if item['children']:
            result.extend(item['children'])

    print((set(x['name'] for x in input_dict) - set(result)).pop())


if __name__ == '__main__':
    main()

