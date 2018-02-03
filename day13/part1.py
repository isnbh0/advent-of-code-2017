import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    def init_stack(ex13):
        dict0 = dict()
        for line in ex13:
            idx, range_ = line.split(': ')
            idx, range_ = int(idx), int(range_)
            dict0[idx] = {'pos': 0, 'dir_': 'd',
                          'range_': range_}
        return dict0    

    def adv_time(ex13):
        for key in ex13.keys():
            if ex13[key]['dir_'] == 'd':
                ex13[key]['pos'] += 1
                if ex13[key]['pos'] >= ex13[key]['range_']-1:
                    ex13[key]['dir_'] = 'u'
            elif ex13[key]['dir_'] == 'u':
                ex13[key]['pos'] -= 1
                if ex13[key]['pos'] <= 0:
                    ex13[key]['dir_'] = 'd'
        return ex13

    def run_13(ex13):
        curr = -1
        end = max(ex13.keys())
        sev = 0
        
        while curr <= end:
            curr += 1
            if curr in ex13.keys() and ex13[curr]['pos'] == 0:
                sev += ex13[curr]['range_'] * curr
            ex13 = adv_time(ex13)
        return sev

    ex13_0 = get_input_by_lines(13)
    ex13 = init_stack(ex13_0)

    print(run_13(ex13))

if __name__ == '__main__':
    main()

