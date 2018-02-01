import sys
sys.path.append('..')
from get_input import get_input_by_lines

from itertools import combinations
from functools import reduce


def main():
    def isanagram(str1, str2):
        return sorted(list(str1)) == sorted(list(str2))

    ex4_0 = get_input_by_lines(4)
    ex4 = [x.split(' ') for x in ex4_0]

    print(len(ex4) - sum([reduce((lambda x, y: x or y),
                                 [isanagram(*x) for x in combinations(elem, 2)])
                          for elem in ex4]))

if __name__ == '__main__':
    main()

