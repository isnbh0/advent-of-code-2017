import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    ex9_0 = get_input_by_lines(9)
    ex9 = ex9_0[0]

    def score_group(group):
        score = 0
        
        left_cnt = 0
        
        in_garbage = False
        ignore_next = False
        
        garbage_cnt = 0
        
        for idx, char in enumerate(group):
            if in_garbage:
                if ignore_next:
                    ignore_next = False
                    pass
                elif char == '>':
                    in_garbage = False
                elif char == '!':
                    ignore_next = True
                else:
                    garbage_cnt += 1
            elif char == '<':
                in_garbage = True
            elif char == '{':
                left_cnt += 1
            elif char == '}':
                score += left_cnt
                left_cnt -= 1
            elif char == ',':
                pass
            else:
                pass
        return score, garbage_cnt

    print(score_group(ex9)[1])

if __name__ == '__main__':
    main()

