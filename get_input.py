#! /home/aeatda/anaconda3/vim/python

import re

def get_input_by_lines(prob, strip=True):
    lines = []

    with open('prob{}.txt'.format(prob), 'r') as prob_input:
        for line in prob_input:
            line = re.sub(r'\t', ',', line)
            if strip:
                lines.append(line.strip())
    return lines

