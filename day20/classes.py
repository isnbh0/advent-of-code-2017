import numpy as np
import re
from collections import Counter

class Particle():
    def __init__(self,
                 pos=(0, 0, 0),
                 vel=(0, 0, 0),
                 acc=(0, 0, 0),
                 infostr=None,
                 id_=0):
        if infostr:
            pos, vel, acc\
            = list(map(lambda x:
            list(map(int, re.search(r'\w=<(.+)>', x)
                     .group(1).split(','))),\
         infostr))
        
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.acc = np.array(acc)
        self.id_ = id_
    
    def move(self):
        self.vel += self.acc
        self.pos += self.vel
        return self.pos
    
    def manhattan(self):
        return np.abs(self.pos).sum()
    
    def __repr__(self):
        return 'p={}'.format(self.pos)+' '\
             + 'v={}'.format(self.vel)+' '\
             + 'a={}'.format(self.acc)+' '\
             + 'id {}'.format(self.id_)


class ParticleSet():
    def __init__(self, infostrs):
        self.particles = list(map(lambda i, x: Particle(infostr=x, id_=i),\
                                 range(len(infostrs)), infostrs))
        return
    
    def step(self, collisions=True):
        for p in self.particles:
            p.move()
        if collisions:
            poslist = [tuple(p.pos) for p in self.particles]
            self.particles = [p for p in self.particles\
                             if Counter(poslist)[tuple(p.pos)] == 1]
        return

