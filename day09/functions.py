def score_group(group):
    score = 0
    
    left_cnt = 0
    
    in_garbage = False
    ignore_next = False
    
    garbage_cnt = 0
    
    for idx, char in enumerate(group):
        if in_garbage:
            if ignore_next:
                ignore_next = False
                pass
            elif char == '>':
                in_garbage = False
            elif char == '!':
                ignore_next = True
            else:
                garbage_cnt += 1
        elif char == '<':
            in_garbage = True
        elif char == '{':
            left_cnt += 1
        elif char == '}':
            score += left_cnt
            left_cnt -= 1
        elif char == ',':
            pass
        else:
            pass
    return score, garbage_cnt

