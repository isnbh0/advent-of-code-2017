def dictify(ex12):
    outdict = dict()    
    
    for line in ex12:
        id_, connections = line.split(' <-> ')
        id_ = int(id_)
        connections = [int(x) for x in connections.split(', ')]
        outdict[id_] = connections
    return outdict

def get_nbrs(input_dict, id_, group_now):
    id_nbrs = [x for x in input_dict[id_] if x not in group_now]
    nbrs = []
    
    if not id_nbrs:
        nbrs.append(id_)
    else:
        nbrs.append(id_)
        for xx in id_nbrs:
            group_now.append(xx)
            nbrs.extend(get_nbrs(input_dict, xx, group_now))
    return set(nbrs) 

