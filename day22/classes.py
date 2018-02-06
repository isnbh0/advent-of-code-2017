import numpy as np


class VirusGrid():
    def __init__(self, grid):
        self.states = dict()
        
        offset = grid.shape[0] // 2        
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                self.states[(j-offset, offset-i)] = grid[i, j]
                
        self.virus_pos = (0, 0)
        
        # DIRS[virus_dir] is direction
        # turn right: virus_dir = (virus_dir + 1) % 4
        # turn lefft: virus_dir = (virus_dir - 1) % 4
        self.DIRS = 'urdl'
        self.virus_dir = 0
        
        self.DIR_KEY = {
            'u' : (0, 1),
            'r' : (1, 0),
            'd' : (0, -1),
            'l' : (-1, 0)
        }
        
        self.infect_cnt = 0
        return
    
    def turn(self, dir_):
        if dir_ in 'Rr':
            self.virus_dir = (self.virus_dir + 1) % 4
        elif dir_ in 'Ll':
            self.virus_dir = (self.virus_dir - 1) % 4
        elif dir_ in 'Bb':
            self.virus_dir = (self.virus_dir + 2) % 4
        elif dir_ in 'Ff':
            pass        
        else:
            raise Exception("Can only turn L, R, B, F")
        return
    
    def burst(self):
        if self.virus_pos in self.states.keys()\
        and self.states[self.virus_pos] == '#':
            self.turn('r')
            self.states[self.virus_pos] = '.'
        else:
            self.turn('l')
            self.states[self.virus_pos] = '#'
            self.infect_cnt += 1
        
        dir_offset = self.DIR_KEY[self.DIRS[self.virus_dir]]
        self.virus_pos = tuple(np.array(self.virus_pos)\
                              +np.array(dir_offset))
        return

    # burst method for part 2
    def burstv2(self):
        if self.virus_pos in self.states.keys()\
        and self.states[self.virus_pos] != '.':
            if self.states[self.virus_pos] == '#':
                self.turn('r')
                self.states[self.virus_pos] = 'F'
            elif self.states[self.virus_pos] == 'W':
                self.turn('f')
                self.states[self.virus_pos] = '#'
                self.infect_cnt += 1
            elif self.states[self.virus_pos] == 'F':
                self.turn('b')
                self.states[self.virus_pos] = '.'
        else:
            self.turn('l')
            self.states[self.virus_pos] = 'W'
        
        dir_offset = self.DIR_KEY[self.DIRS[self.virus_dir]]
        self.virus_pos = tuple(np.array(self.virus_pos)\
                              +np.array(dir_offset))
        return

