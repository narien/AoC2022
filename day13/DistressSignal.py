import copy
from functools import cmp_to_key
import json

def myEval(p1, p2):
    if type(p1) != list and type(p2) != list:
        if p1 == p2:
            return 0
        elif p1 < p2:
            return -1
        else:
            return 1

    if type(p1) == list and type(p2) != list:
        p2 = [p2]
    if type(p1) != list and type(p2) == list:
        p1 = [p1]

    for i in range(len(p1)):
        if i < len(p2):
            res = myEval(p1[i], p2[i])
            if type(res) is bool:
                return res
            if res == 0:
                continue
            elif res == -1:
                return True
            elif res == 1:
                return False
            else:
                return False
        else:
            return False
    return 0 if len(p1) == len(p2) else True

def myCompare(p1, p2):
    if myEval(p1, p2):
        return -1
    return 1

def evalPairs(pairs):
    currIndex = 0
    total = 0
    for p in pairs:
        currIndex += 1
        res = myEval(p[0], p[1])
        if type(res) is bool and res:
            total += currIndex
    print('part 1 sum: ' + str(total))


if __name__ == '__main__':
    with open('day13/input.txt') as f:
        lines = [line.strip() for line in f]

    pairs = []
    for i in range(0, len(lines), 3):
        pairs.append((copy.deepcopy(json.loads(lines[i])), copy.deepcopy(json.loads(lines[i+1]))))

    evalPairs(pairs)

    part2List = [[[2]], [[6]]]
    for line in lines:
        if len(line) > 0:
            part2List.append(copy.deepcopy(json.loads(line)))

    sortedList = sorted(part2List, key=cmp_to_key(myCompare))
    dPack1 = sortedList.index([[2]]) + 1
    dPack2 = sortedList.index([[6]]) + 1
    print('decoder key is: ' + str(dPack1*dPack2))

