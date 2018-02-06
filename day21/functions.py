import numpy as np


def d8(arr, as_str=False):
    if isinstance(arr, str):
        arr = str_to_sq(arr)
    arrs = []
    
    for i in range(8):
        arr_res = arr
        if as_str:
            arr_res = sq_to_str(arr_res)
        arrs.append(arr_res)
        
        arr = np.rot90(arr)
        if i == 3:
            arr = np.fliplr(arr)
    return arrs    

def dictify(rules):
    return dict(list(map(lambda z: tuple(map(lambda x: x.replace('/', ''),
                                             z.split(' => '))),
                         rules)))

def str_to_sq(str0):
    side_len = int(len(str0)**0.5)
    return np.array(list(str0)).reshape(side_len, side_len)

def sq_to_str(sq0):
    return ''.join(sq0.flatten())

def divvy(arr, dim):
    # Input: square ndarray with dim multiple of 2 or 3
    # Output: list of square ndarrays with dim = 2x2 or 3x3
    size = arr.shape[0]
    return list(arr.reshape(size//dim, dim, -1, dim)\
                   .swapaxes(1, 2)\
                   .reshape(-1, dim, dim))

def reverse_divvy(list_):
    # Input: list of square ndarrays
    # Assumption: len of list is a square number
    # Output: single square ndarray
    arr = np.array(list_)
    dim = list_[0].shape[0]
    size = int(np.sqrt(len(list_))) * dim
    return arr.reshape(size//dim, -1, dim, dim)\
              .swapaxes(1, 2)\
              .reshape(size, size)

def subst(piece, key):
    forms = d8(piece, as_str=True)
    for f in forms:
        if f in key.keys():
            return key[f]
    return False

def transform(arr, key):
    size = arr.shape[0]

    if size % 2 == 0:
        dim = 2
    elif size % 3 == 0:
        dim = 3
    else:
        raise Exception("Dimensions must be multiple of 2 or 3")

    pieces = divvy(arr, dim)
    new_pieces = [str_to_sq(subst(x, key)) for x in pieces]
    new_arr = reverse_divvy(new_pieces)
    
    return new_arr
