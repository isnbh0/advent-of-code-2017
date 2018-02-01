import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    ex5_0 = get_input_by_lines(5)
    ex5 = [int(x) for x in ex5_0]

    idx = 0
    count = 0
    errors = False

    while not errors:
        try:
            jump_val = ex5[idx]
            ex5[idx] += 1
            idx += jump_val
            count += 1
        except:
            errors = True
            continue

    print(count)


if __name__ == '__main__':
    main()

