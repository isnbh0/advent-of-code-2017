import sys
sys.path.append('..')
from get_input import get_input_by_lines

def get_repeat_sum2(num):
    numlen = len(num)
    assert not numlen & 1
    
    numlist = str(num) + str(num)[0]
    
    sum_ = 0
    for idx, digit in enumerate(numlist[:-1]):
        goal = (idx+numlen//2) % numlen
        sum_ += int(digit == numlist[goal])*int(digit)
    
    return sum_

ex1 = ','.join(get_input_by_lines(1))
print(get_repeat_sum2(ex1))

