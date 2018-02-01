import sys
sys.path.append('..')
from get_input import get_input_by_lines

import re


def main():

    def dictify(lines):
        name = re.search(r'\w+', lines).group(0)
        weight = int(re.search(r'\((\d+)\)', lines).group(1))
        children = re.search(r'-\> (.+)$', lines)
        if children:
            children = children.group(1).split(', ')
        return {'name': name, 'weight' : weight, 'children' : children}

    def solve7(input_lines):
        input_dict = [dictify(x) for x in input_lines]

        result = []
        for item in input_dict:
            if item['children']:
                result.extend(item['children'])

        return set(x['name'] for x in input_dict) - set(result)

    def dictify2(lines):
        name = re.search(r'\w+', lines).group(0)
        weight = int(re.search(r'\((\d+)\)', lines).group(1))
        children = re.search(r'-\> (.+)$', lines)
        if children:
            children = children.group(1).split(', ')
        return name, weight, children

    def process7(a):
        resdict = {}
        
        for item in a:
            n, w, c = dictify2(item)
            resdict[n] = {'weight' : w, 'children' : c}
        
        return resdict

    def get_weight(mainlist, name):
        if not mainlist[name]['children']:
            return mainlist[name]['weight']
        else:
            return mainlist[name]['weight'] + sum([get_weight(mainlist, child) for child in mainlist[name]['children']])

    def balanced(mainlist, name):
        if not mainlist[name]['children']:
            return True
        else:
            weights = [get_weight(mainlist, child) for child in mainlist[name]['children']]
            return weights.count(weights[0]) == len(weights), weights

    def where_to_go(mainlist, name):
        childlist = mainlist[name]['children']
        if not childlist:
            return None
        else:
            is_balanced, weights = balanced(mainlist, name)
            if is_balanced:
                return []
            elif len(weights) == 2:
                return childlist
            else:
                for idx, item in enumerate(weights):
                    if weights.count(item) == 1:
                        return [childlist[weights.index(item)]]

    def find_wrong(a):
        base = solve7(a).pop()
        mainlist = process7(a)
        
        current_node = base
        parent_node = None
        end_found = False
        
        while not end_found:
            to_go = where_to_go(mainlist, current_node)
            
            if not to_go:
                end_found = True
            else:
                parent_node = current_node
                current_node = to_go[0]
                
        return parent_node, [get_weight(mainlist, c) for c in mainlist[parent_node]['children']]


    ex7_0 = get_input_by_lines(7)
    dict7 = process7(ex7_0)

    print(get_weight(dict7, where_to_go(dict7, find_wrong(ex7_0)[0])[0]))    


if __name__ == '__main__':
    main()

