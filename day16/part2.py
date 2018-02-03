import sys
sys.path.append('..')
from get_input import get_input_by_lines


class Danceline:
    def __init__(self, line):
        self.line = list(line)
        return
    
    def spin(self, num):
        num = int(num)
        self.line = self.line[-1*num:] + self.line[:-1*num]
        return self.line
    
    def exchange(self, code):
        a, b = [int(x) for x in code.split('/')]
        self.line[a], self.line[b] = self.line[b], self.line[a]
        return self.line
    
    def partner(self, code):
        a, b = code.split('/')
        ia = self.line.index(a)
        ib = self.line.index(b)
        self.line[ia], self.line[ib] = self.line[ib], self.line[ia]
        return self.line
    
    def __str__(self):
        return ''.join(self.line)
    
    def act(self, code):
        key, val = code[0], code[1:]
        if key == 's':
            self.line = self.spin(val)
        elif key == 'x':
            self.line = self.exchange(val)
        elif key == 'p':
            self.line = self.partner(val)
        return self.line

    def acts(self, codes):
        for code in codes:
            self.line = self.act(code)
        return self.line
    
    def repeat(self, codes, times):
        for x in range(times):
            self.acts(codes)
            if self.line == startinglist:
                return (x+1)
        return self.line
    
    def permute(self, times, idces):
        for i in range(times):
            self.line = [self.line[idx] for idx in idces]
            if self.line == startinglist:
                return (i+1)
        return self.line

def main():
    global startinglist

    ex16_0 = get_input_by_lines(16)
    ex16 = ex16_0[0].split(',')

    starting = 'abcdefghijklmnop'
    startinglist = list(starting)
    line = Danceline(starting)

    # Cycle repeats after 60 dances; hardcoded 1e9 % 60
    print(''.join(line.repeat(ex16, 40)))

if __name__ == '__main__':
    main()

