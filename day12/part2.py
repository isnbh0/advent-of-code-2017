import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import dictify, get_nbrs


def main():
    ex12_0 = get_input_by_lines(12)
    ex12 = dictify(ex12_0)

    groups = []
    for key in ex12.keys():
        pass_ = False
        for g in groups:
            if key in g:
                pass_ = True
        if pass_:
            continue
        group = get_nbrs(ex12, key, [])
        groups.append(group)
    
    print(len(groups))

if __name__ == '__main__':
    main()

