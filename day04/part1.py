import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    ex4_0 = get_input_by_lines(4)
    ex4 = [x.split(' ') for x in ex4_0]

    print(sum([len(x) == len(set(x)) for x in ex4]))

if __name__ == '__main__':
    main()

