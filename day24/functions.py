from copy import deepcopy as dcopy


def make_bridges(old_comps, port=0, current=[], lvl=0):
    viable = [comp for comp in old_comps if port in comp]
    old_current = dcopy(current)
    
    bridges = []
    
    for comp in viable:
        comps = dcopy(old_comps)
        current = dcopy(old_current)

        comps.remove(comp)
        complist = list(comp)
        complist.remove(port)
        new_port = complist[0]
        
        current.append(comp)
        bridges.append(dcopy(current))

        bridges.extend(
                      make_bridges(dcopy(comps), new_port,
                                   dcopy(current), lvl+1))
    return bridges

