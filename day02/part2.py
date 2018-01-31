import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np


def listdiv(mylist):
    mylist = np.array(sorted(mylist))
    thresh = mylist[-1] // 2
    
    idx = 0
    while mylist[idx] <= thresh:
        filtlist = mylist[mylist/mylist[idx] == mylist//mylist[idx]]
        if len(filtlist) > 1:
            val = filtlist[-1] / mylist[idx]
            break
        idx += 1
    
    return val


ex2_0 = get_input_by_lines(2)
ex2 = np.array([x.split(',') for x in ex2_0]).astype(np.int32)

print(np.apply_along_axis(listdiv, axis=1, arr=ex2).sum())
