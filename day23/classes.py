import numpy as np


class Prog():
    def __init__(self, instrs, v2=False):
        self.idx = 0
        self.instrs = instrs
        
        self.reg = {}
        for let in 'abcdefghi':
            self.reg[let] = 0

        # Options for part 1 and part 2
        self.v2 = v2
        if self.v2:
            self.reg['a'] = 1
        else:
            self.mul_cnt = 0
        return
    
    def _reached_end(self):
        return self.idx < 0\
    or self.idx >= len(self.instrs)
    
    def _increment_idx(self):
        self.idx += 1
        return
    
    def _get_val(self, val):
        try:
            val = int(val)
        except:
            val = self.reg[val]
        return val
    
    def set_(self, key, val):
        self.reg[key] = self._get_val(val)
        return
        
    def sub_(self, key, val):
        self.reg[key] -= self._get_val(val)
        return
    
    def mul_(self, key, val):
        self.reg[key] *= self._get_val(val)
        if not self.v2:
            self.mul_cnt += 1
        return
    
    
    def jnz_(self, key, val):
        key = self._get_val(key)
        if key != 0:
            self.idx += self._get_val(val) - 1
        return
    
    def run(self):
        count = 0

        while (self.idx >= 0)\
        and (self.idx < len(self.instrs)):
            count += 1
            instr = self.instrs[self.idx]
            cmd = instr[0]

            eval_str = "self.{}_(*{})"            
            rcv_val = eval(eval_str.format(instr[0], instr[1:]))   
            self.idx += 1
        return count

