import copy
import json

def myEval(p1, p2):
    if type(p1) == list and type(p2) != list:
        p2 = [p2]
    if type(p1) != list and type(p2) == list:
        p1 = [p1]

    if type(p1) == list and type(p2) == list:
        myEval(p1[0])
    if p1 < p2:
        return True
    return False

def evalPairs(pairs):
    for p in pairs:
        eval(p[0], p[1])
if __name__ == '__main__':
    with open('day13/input.txt') as f:
        lines = [line.strip() for line in f]

    pairs = []
    for i in range(0, len(lines), 3):
        pairs.append((copy.deepcopy(json.loads(lines[i])), copy.deepcopy(json.loads(lines[i+1]))))

    evalPairs(pairs)

