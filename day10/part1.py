import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    ex10_0 = get_input_by_lines(10)
    ex10 = [int(x) for x in ex10_0[0].split(',')]

    def reverse_list(list0, start_idx, rev_len):
        list1 = list0.copy()
        
        end_idx = start_idx + rev_len - 1
        
        for idx in range(rev_len):
            idx1 = (end_idx - idx) % len(list0)
            idx0 = (start_idx + idx) % len(list0)
            list1[idx1] = list0[idx0]
        return list1

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

