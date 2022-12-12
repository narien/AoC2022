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

def foundTop(x, y, tMap):
    if tMap[y][x] == 'E':
        return True
    return False

def addNewSteps(x, y, stepCount, queue, tMap, haveVisited):
    if x < len(tMap[0]) - 1 and (x+1, y) not in haveVisited:
        if abs(ord(tMap[y][x]) - ord(tMap[y][x+1])) <= 1 or tMap[y][x] in ['y', 'z'] and tMap[y][x+1] == 'E':
            queue.append((x+1, y, stepCount))
            haveVisited.add((x+1, y))
    if x > 0 and (x-1, y) not in haveVisited:
        if abs(ord(tMap[y][x]) - ord(tMap[y][x-1])) <= 1 or tMap[y][x] in ['y', 'z'] and tMap[y][x-1] == 'E':
            queue.append((x-1, y, stepCount))
            haveVisited.add((x-1, y))
    if y < len(tMap) - 1 and (x, y+1) not in haveVisited:
        if abs(ord(tMap[y][x]) - ord(tMap[y+1][x])) <= 1 or tMap[y][x] in ['y', 'z'] and tMap[y+1][x] == 'E':
            queue.append((x, y+1, stepCount))
            haveVisited.add((x, y+1))
    if y > 0 and (x, y-1) not in haveVisited:
        if abs(ord(tMap[y][x]) - ord(tMap[y-1][x])) <= 1 or tMap[y][x] in ['y', 'z'] and tMap[y-1][x] == 'E':
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

if __name__ == '__main__':
    with open('day12/input.txt') as f:
        lines = [line.strip() for line in f]
    tMap = buildMap(lines)
    x, y = findStart(tMap)
    tMap[y][x] = 'a'
    print('shortest path is: ' + str(traverse(tMap, x, y)))
