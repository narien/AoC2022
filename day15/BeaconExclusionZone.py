def trimCoord(c, end):
    return int(c[2:]) if end else int(c[2:-1])

def parseInput(lines):
    positions = dict()
    for line in lines:
        _, _, sX, sY, _, _, _, _, bX, bY = line.split()
        positions[(trimCoord(sX, False), trimCoord(sY, False))] = (trimCoord(bX, False), trimCoord(bY, True))
    return positions

def manhattanDist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def generateRowOfInterestCoords(positions, rowOfInterest):
    invalidPoints = set()
    for key, val in positions.items():
        dist = manhattanDist(key, val)
        if key[1] - dist < rowOfInterest and key[1] + dist > rowOfInterest:
            for x in range(key[0]-dist, key[0]+dist):
                    pointDist = manhattanDist(key, (x,rowOfInterest))
                    if pointDist <= dist and (x,rowOfInterest) not in positions.values():
                        invalidPoints.add((x,rowOfInterest))
    return invalidPoints

def calcPartOne(invalidPoints, rowOfInterest):
    interestingRow = set()
    for p in invalidPoints:
        if p[1] == rowOfInterest:
            interestingRow.add(p)
    print('invalid coords on row ' + str(rowOfInterest) + ": " + str(len(interestingRow)))

def checkEveryBorder(positions, minC, maxC):
    sensorDists = dict()
    for key, val in positions.items():
        dist = manhattanDist(key, val)
        sensorDists[key] = dist
    interestingPoints = set()
    for key, val in positions.items():
        dist = manhattanDist(key, val) + 1
        for i in range(dist + 1):
            c = (key[0] - (dist - i), key[1] + i)
            if c[0] > minC and c[0] < maxC and c[1] > minC and c[1] < maxC:
                interestingPoints.add(c)
        for i in range(dist + 1):
            c = (key[0] + i, key[1] - (dist - i))
            if c[0] > minC and c[0] < maxC and c[1] > minC and c[1] < maxC:
                interestingPoints.add(c)
        for i in range(dist, -1, -1):
            c = (key[0] + i, key[1] - (dist - i))
            if c[0] > minC and c[0] < maxC and c[1] > minC and c[1] < maxC:
                interestingPoints.add(c)
        for i in range(dist, -1, -1):
            c = (key[0] - (dist - i), key[1] + i)
            if c[0] > minC and c[0] < maxC and c[1] > minC and c[1] < maxC:
                interestingPoints.add(c)
    for p in interestingPoints:
        badCoord = False
        for key, val in sensorDists.items():
            dist = manhattanDist(p, key)
            if dist <= val:
                badCoord = True
                break
        if badCoord == False:
            return p

def calcTuningFreq(coord):
    return coord[0]*4000000 + coord[1]

if __name__ == '__main__':
    with open('day15/input.txt') as f:
        lines = [line.strip() for line in f]
    positions = parseInput(lines)
    rowOfInterest = 2000000 if len(positions) > 14 else 10
    invalidPoints = generateRowOfInterestCoords(positions, rowOfInterest)
    calcPartOne(invalidPoints, rowOfInterest)

    minCoord = 0
    maxCoord = 4000000 if len(positions) > 14 else 20

    coord = checkEveryBorder(positions, minCoord, maxCoord)
    print('tuning frequency is: ' + str(calcTuningFreq(coord)))
