lr = {' left' : -1, 'right' : 1}

# Simple encode_instr
# Hardcoded to fit Advent of Code input format 
def encode_instr(text):
    instr = {}
    instr[0] = text[0][-2]
    
    for i in range(3, 63, 10):
        cond_dict = dict()

        cond_dict[int(text[i+1][-2])] = (int(text[i+2][-2]),
                                        lr[text[i+3][-6:-1]],
                                        text[i+4][-2])
        cond_dict[int(text[i+5][-2])] = (int(text[i+6][-2]),
                                        lr[text[i+7][-6:-1]],
                                        text[i+8][-2])
        instr[text[i][-2]] = cond_dict
    return instr

