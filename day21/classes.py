import numpy as np
import re
from collections import Counter

from functions import str_to_sq, transform


ON_CHAR = '#'
OFF_CHAR = '.'

INIT_ARR = np.array(list('''.#.
..#
###'''.replace('\n', ''))).reshape(3, 3)


class PixelGrid():
    def __init__(self, key_, arr_=None, str_=None):
        if arr_ is not None:
            self.arr_ = arr_
        elif str_:
            self.arr_ = str_to_sq(str_)
        else:
            raise Exception("Must pass arr_ or str_")
        self.key_ = key_
        self.iters = 0
        return
    
    def iterate(self, n=1):
        for i in range(n):
            self.iters += 1
            self.arr_ = transform(self.arr_, self.key_)
        return
    
    def get_count(self):
        return (self.arr_ == ON_CHAR).sum()

