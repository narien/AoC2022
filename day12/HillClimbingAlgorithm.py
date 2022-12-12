import sys
haveVisited = set()

def buildMap(lines):
    tMap = []
    for line in lines:
        tMap.append(list(line))
    return tMap

def findStart(tMap):
    for y in range(len(tMap)):
        for x in range(len(tMap[y])):
            if(tMap[y][x] == 'S'):
                return x, y

def traverse(tMap, x, y, stepCount):
    haveVisited.add((x,y))
    if tMap[y][x] == 'E':
        return stepCount
    stepCount += 1

    minCount = 999999999
    if x < len(tMap[0]) - 1 and (x+1, y) not in haveVisited:
        if abs(ord(tMap[y][x]) - ord(tMap[y][x+1])) <= 1 or tMap[y][x] in ['y', 'z'] and tMap[y][x+1] == 'E':
            count = traverse(tMap, x+1, y, stepCount)
            if count < minCount:
                minCount = count
    
    if x > 0 and (x-1, y) not in haveVisited:
        if abs(ord(tMap[y][x]) - ord(tMap[y][x-1])) <= 1 or tMap[y][x] in ['y', 'z'] and tMap[y][x-1] == 'E':
            count = traverse(tMap, x-1, y, stepCount)
            if count < minCount:
                minCount = count

    if y < len(tMap) - 1 and (x, y+1) not in haveVisited:
        if abs(ord(tMap[y][x]) - ord(tMap[y+1][x])) <= 1 or tMap[y][x] in ['y', 'z'] and tMap[y+1][x] == 'E':
            count = traverse(tMap, x, y+1, stepCount)
            if count < minCount:
                minCount = count
    
    if y > 0 and (x, y-1) not in haveVisited:
        if abs(ord(tMap[y][x]) - ord(tMap[y-1][x])) <= 1 or tMap[y][x] in ['y', 'z'] and tMap[y-1][x] == 'E':
            count = traverse(tMap, x, y-1, stepCount)
            if count < minCount:
                minCount = count
    return minCount
    





if __name__ == '__main__':
    with open('day12/input.txt') as f:
        lines = [line.strip() for line in f]
    tMap = buildMap(lines)
    x, y = findStart(tMap)
    tMap[y][x] = 'a'
    sys.setrecursionlimit(6000)
    print('shortest path is: ' + str(traverse(tMap, x, y, 0)))
