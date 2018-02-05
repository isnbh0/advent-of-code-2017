import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    class ProgPair():
        def __init__(self, instrs):
            self.p0 = Prog(0, instrs)
            self.p1 = Prog(1, instrs)
            self.p1_snd = 0
            self.count = 0
            return
        
        def _finished(self):
            return (self.p0.waiting or self.p0._reached_end())\
               and (self.p1.waiting or self.p1._reached_end())
        
        def run(self):
            while not self._finished():
                self.count += 1

                # p0
                if self.p0.waiting and not self.p0.in_queue:
                        continue
                instr = self.p0.instrs[self.p0.idx]
                cmd = instr[0]
                eval_str = "self.p0.{}_(*{})"            
                snd_val = eval(eval_str.format(instr[0], instr[1:]))               
                if isinstance(snd_val, int):
                    self.p1.in_queue.append(snd_val)
                if not self.p0.waiting:
                    self.p0._increment_idx()
                
                # p1
                if self.p1.waiting and not self.p1.in_queue:
                        continue
                instr = self.p1.instrs[self.p1.idx]
                cmd = instr[0]
                eval_str = "self.p1.{}_(*{})"            
                snd_val = eval(eval_str.format(instr[0], instr[1:]))   
                if isinstance(snd_val, int):
                    self.p0.in_queue.append(snd_val)
                    self.p1_snd += 1
                if not self.p1.waiting:
                    self.p1._increment_idx()
            return self.p0.idx, self.p1.idx, self.p1_snd, self.count


    class Prog():
        def __init__(self, prog_id, instrs):
            self.idx = 0
            self.prog_id = prog_id
            self.instrs = instrs
            self.waiting = False
            self.in_queue = []
            
            self.reg = {}
            for let in 'abcdefghijklmnoqrstuvwxyz':
                self.reg[let] = 0
            self.reg['p'] = self.prog_id
            
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
        
        def enqueue(self, val):
            self.in_queue.append(val)
            return
     
        def snd_(self, val):
            return self._get_val(val)

        def rcv_(self, key):
            if self.in_queue:
                self.reg[key] = self.in_queue.pop(0)
                self.waiting = False
            else:
                self.waiting = True
            return
        
        def set_(self, key, val):
            self.reg[key] = self._get_val(val)
            return
            
        def add_(self, key, val):
            self.reg[key] += self._get_val(val)
            return
        
        def mul_(self, key, val):
            self.reg[key] *= self._get_val(val)
            return
        
        def mod_(self, key, val):
            self.reg[key] %= self._get_val(val)
            return
        
        def jgz_(self, key, val):
            key = self._get_val(key)
            if key > 0:
                self.idx += self._get_val(val) - 1
            return


    ex18_0 = get_input_by_lines(18)
    ex18 = list(map(lambda x: x.split(), ex18_0))

    pair = ProgPair(ex18)
    print(pair.run()[2])
    

if __name__ == '__main__':
    main()

