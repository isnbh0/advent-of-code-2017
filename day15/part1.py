import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    print("This code takes about 70s to run. Ctrl+C to break before then.")

    def bit16(int0):
        return '{:0>32}'.format(str(bin(int0))[2:])[-16:]

    afac = 16807
    bfac = 48271
    n = 2**31 - 1

    ex15_0 = get_input_by_lines(15)
    a, b = int((ex15_0[0].split())[-1]), int((ex15_0[1].split())[-1])

    count = 0

    for it in range(40000000):
        a = a*afac % n
        b = b*bfac % n
        if bit16(a) == bit16(b):
            count += 1
    print(count)

if __name__ == '__main__':
    main()

