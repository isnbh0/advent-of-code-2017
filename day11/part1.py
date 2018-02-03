import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    ex11_0 = get_input_by_lines(11)
    ex11 = ex11_0[0].split(',')

    def simplify_coords(i, j, k):
        # i : n
        # j : se
        # k : sw
        # i + j + k -> 0
        while max(min(i, j), min(j, k), min(k, i)) > 0:
            i, j, k = i-1, j-1, k-1
        while min(max(i, j), max(j, k), max(k, i)) < 0:
            i, j, k = i+1, j+1, k+1
        return abs(i) + abs(j) + abs(k) 

    def make_coords(dirs):
        max_d = 0
        i, j, k = 0, 0, 0
        n, s, se, nw, sw, ne = 0, 0, 0, 0, 0, 0
        
        for d in dirs:
            if d == 'n':
                i += 1
                n += 1
            elif d == 's':
                i -= 1
                s += 1
            elif d == 'se':
                j += 1
                se += 1
            elif d == 'nw':
                j -= 1
                nw += 1
            elif d == 'sw':
                k += 1
                sw += 1
            elif d == 'ne':
                k -= 1
                ne += 1
            cur_d = simplify_coords(i, j, k)
            if cur_d > max_d:
                max_d = cur_d
        return i, j, k, n, s, se, nw, sw, ne, max_d

    print(simplify_coords(*make_coords(ex11)[:3]))

if __name__ == '__main__':
    main()

