import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    ex8_0 = get_input_by_lines(8)
    ex8 = ex8_0 

    instr_list = [x.split() for x in ex8]
    reg_list = [x[0] for x in instr_list]
    regs = dict(zip(set(reg_list), [0]*len(set(reg_list))))

    for i in instr_list:
        i_new = [x.replace('inc', '+').replace('dec', '-') for x in i]
        exec("regs['{0}'] = regs['{0}'] {1} {2} {3} regs['{4}'] {5} {6} else regs['{0}']".format(*i_new))

    print(max(regs.values()))

if __name__ == '__main__':
    main()

