import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    class Register():
        def __init__(self, instrs):
            self.played = []
            self.reg = {}
            self.idx = 0
            self.instrs = instrs
            
            for let in 'abcdefghijklmnopqrstuvwxyz':
                self.reg[let] = 0
            return
            
        
        def _print_errormsg(self):
            print("Key doesn't exist. Doing nothing.")
            return
        
        def _get_val(self, val):
            try:
                val = int(val)
            except:
                val = self.reg[val]
            return val
        
        def run(self):
            while (self.idx >= 0)\
            and (self.idx < len(self.instrs)):
                instr = self.instrs[self.idx]
                cmd = instr[0]

                eval_str = "self.{}_(*{})"            
                rcv_val = eval(eval_str.format(instr[0], instr[1:]))   
                
                if cmd != 'jgz':
                    self.idx += 1

                if rcv_val:
                    return rcv_val
        
        def snd_(self, key):
            try:
                self.played.append(self.reg[key])
            except:
                self._print_errormsg()
            return

        def set_(self, key, val):
            try:
                self.reg[key] = self._get_val(val)
            except Exception as e:
                self._print_errormsg()
                print(e)
            return
            
        def add_(self, key, val):
            try:
                self.reg[key] += self._get_val(val)
            except:
                self._print_errormsg()
            return
        
        def mul_(self, key, val):
            try:
                self.reg[key] *= self._get_val(val)
            except:
                self._print_errormsg()
            return
        
        def mod_(self, key, val):
            try:
                self.reg[key] %= self._get_val(val)
            except:
                self._print_errormsg()
            return
        
        def rcv_(self, key):
            try:
                val = self.reg[key]
                if val != 0:
                    rcv_val = self.played[-1]
                    return rcv_val
            except:
                self._print_errormsg()
            return
        
        def jgz_(self, key, val):
            try:
                if self.reg[key] > 0:
                    self.idx += self._get_val(val)
                else:
                    self.idx += 1
            except:
                self._print_errormsg()
            return

    ex18_0 = get_input_by_lines(18)
    ex18 = list(map(lambda x: x.split(), ex18_0))

    register = Register(ex18)
    print(register.run())
    

if __name__ == '__main__':
    main()

