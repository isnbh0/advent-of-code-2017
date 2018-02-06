import sys
sys.path.append('..')
from get_input import get_input_by_lines

import numpy as np


def main():
    class Map():
        def __init__(self, map_):
            self.map_ = map_
            self.dir_ = 'd'
            self.pos_ = np.array([0, 0])
            self.letters = []
            self.dirkey = {
                'u' : np.array([-1, 0]),
                'r' : np.array([0, 1]),
                'd' : np.array([1, 0]),
                'l' : np.array([0, -1]),
            }
        
        def _nonempty_nbr(self, newdir):
            try:
                nonempty =\
                self.map_[tuple(self.pos_ + self.dirkey[newdir])] != ' '
            except:
                nonempty = False
            return nonempty
        
        def find_start(self):
            return np.array([0, np.asscalar(
                np.where(self.map_[0] == '|')[0])])
        
        def set_pos(self, coord):
            self.pos_ = coord
            return
        
        def change_dir(self):
            if self.dir_ in 'ud':
                newdirs = 'lr'
            elif self.dir_ in 'lr':
                newdirs = 'ud'
            else:
                raise Exception("Invalid direction")
            
            for newdir in newdirs:
                if self._nonempty_nbr(newdir):
                    self.dir_ = newdir
            return
        
        def step(self):
            current = self.map_[tuple(self.pos_)]
            if current == '+':
                self.change_dir()
            elif current.isalpha():
                self.letters.append(current)
            elif current == ' ':
                # Reached end or something wrong
                return True
            
            self.pos_ += self.dirkey[self.dir_]
            return

    ex19_0 = get_input_by_lines(19, strip=False)
    ex19 = np.array(list(map(list, ex19_0)))

    map19 = Map(ex19)
    map19.set_pos(map19.find_start())

    finished = False
    cnt = 0
    while not finished:
        finished = map19.step()
        if not finished:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()

