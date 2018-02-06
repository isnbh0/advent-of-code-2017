import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import reverse_list


def main():
    ex10_0 = get_input_by_lines(10)
    ex10 = [int(x) for x in ex10_0[0].split(',')]

    curr_idx = 0
    skip_size = 0

    mylist = list(range(256)) 

    for val in ex10:
        mylist = reverse_list(mylist, curr_idx, val)
        curr_idx += (val + skip_size)
        skip_size += 1

    print(mylist[0] * mylist[1])
    

if __name__ == '__main__':
    main()

