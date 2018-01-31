import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    def get_repeat_sum(num):
        numlist = str(num) + str(num)[0]
        sum_ = 0
        for idx, digit in enumerate(numlist[:-1]):
            sum_ += int(digit == numlist[idx+1])*int(digit)
        return sum_

    ex1 = ','.join(get_input_by_lines(1))
    print(get_repeat_sum(ex1))

if __name__ == '__main__':
    main()

