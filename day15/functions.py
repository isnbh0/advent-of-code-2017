def bit16(int0):
    return '{:0>32}'.format(str(bin(int0))[2:])[-16:]

