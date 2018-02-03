import sys
sys.path.append('..')
from get_input import get_input_by_lines


def main():
    ex12_0 = get_input_by_lines(12)
    ex12 = ex12_0

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
        
    print(len(get_nbrs(dictify(ex12), 0, [])))

if __name__ == '__main__':
    main()

