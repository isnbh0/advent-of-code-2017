import sys
sys.path.append('..')
from get_input import get_input_by_lines

from functions import bit16


afac = 16807
bfac = 48271
adiv = 4
bdiv = 8
n = 2**31 - 1

def main():
    print("This code takes about 25s to run. Ctrl+C to break before then.")

    ex15_0 = get_input_by_lines(15)
    a, b = int((ex15_0[0].split())[-1]), int((ex15_0[1].split())[-1])

    count = 0
    for it in range(5000000):
        while a % adiv:
            a = a*afac % n
        while b % bdiv:
            b = b*bfac % n
        if bit16(a) == bit16(b):
            count += 1
        a = a*afac % n
        b = b*bfac % n
    print(count)

if __name__ == '__main__':
    main()

