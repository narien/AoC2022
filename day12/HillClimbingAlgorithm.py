import sys

def buildMap(lines):
    tMap = []
    for line in lines:
        tMap.append(list(line))
    return tMap

def findStart(tMap):
    suitableStarts = []
    for y in range(len(tMap)):
        for x in range(len(tMap[y])):
            if(tMap[y][x] == 'S'):
                suitableStarts.append((x,y))
    for y in range(len(tMap)):
        for x in range(len(tMap[y])):
            if(tMap[y][x] == 'a'):
                suitableStarts.append((x,y))
    return suitableStarts

def foundTop(x, y, tMap):
    if tMap[y][x] == 'E':
        return True
    return False

def addNewSteps(x, y, stepCount, queue, tMap, haveVisited):
    if x < len(tMap[0]) - 1 and (x+1, y) not in haveVisited:
        if ord(tMap[y][x]) - ord(tMap[y][x+1]) >= -1 or tMap[y][x] in ['y', 'z'] and tMap[y][x+1] == 'E':
            queue.append((x+1, y, stepCount))
            haveVisited.add((x+1, y))
    if x > 0 and (x-1, y) not in haveVisited:
        if ord(tMap[y][x]) - ord(tMap[y][x-1]) >= -1 or tMap[y][x] in ['y', 'z'] and tMap[y][x-1] == 'E':
            queue.append((x-1, y, stepCount))
            haveVisited.add((x-1, y))
    if y < len(tMap) - 1 and (x, y+1) not in haveVisited:
        if ord(tMap[y][x]) - ord(tMap[y+1][x]) >= -1 or tMap[y][x] in ['y', 'z'] and tMap[y+1][x] == 'E':
            queue.append((x, y+1, stepCount))
            haveVisited.add((x, y+1))
    if y > 0 and (x, y-1) not in haveVisited:
        if ord(tMap[y][x]) - ord(tMap[y-1][x]) >= -1 or tMap[y][x] in ['y', 'z'] and tMap[y-1][x] == 'E':
            queue.append((x, y-1, stepCount))
            haveVisited.add((x, y-1))

def traverse(tMap, x, y):
    haveVisited = set()
    haveVisited.add((x, y))
    queue = [(x, y, 0)]
    while len(queue):
        x, y, stepCount = queue.pop(0)
        if foundTop(x, y, tMap):
            return stepCount
        addNewSteps(x, y, stepCount + 1, queue, tMap, haveVisited)
    return sys.maxsize

if __name__ == '__main__':
    with open('day12/input.txt') as f:
        lines = [line.strip() for line in f]
    tMap = buildMap(lines)
    starts = findStart(tMap)
    sX, sY = starts[0]
    tMap[sY][sX] = 'a'

    counts = set()
    for x, y in starts:
        count = traverse(tMap, x, y)
        if x == sX and y == sY:
            print('shortest path from S is: ' + str(count))
        counts.add(count)
    print('shortest path from any a is: ' + str(min(counts)))
