import numpy as np


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

