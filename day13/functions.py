def init_stack(input_):
    dict0 = dict()
    for line in input_:
        idx, range_ = line.split(': ')
        idx, range_ = int(idx), int(range_)
        dict0[idx] = {'pos': 0, 'dir_': 'd',
                      'range_': range_}
    return dict0    

def adv_time(input_):
    for key in input_.keys():
        if input_[key]['dir_'] == 'd':
            input_[key]['pos'] += 1
            if input_[key]['pos'] >= input_[key]['range_']-1:
                input_[key]['dir_'] = 'u'
        elif input_[key]['dir_'] == 'u':
            input_[key]['pos'] -= 1
            if input_[key]['pos'] <= 0:
                input_[key]['dir_'] = 'd'
    return input_

def get_severity(input_):
    curr = -1
    end = max(input_.keys())
    sev = 0
    
    while curr <= end:
        curr += 1
        if curr in input_.keys() and input_[curr]['pos'] == 0:
            sev += input_[curr]['range_'] * curr
        input_ = adv_time(input_)
    return sev

