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
        print(key)
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
    print(len(interestingRow))

def generateInterestCoords(positions, minCoord, maxCoord):
    invalidPoints = set()
    for key, val in positions.items():
        print(key)
        dist = manhattanDist(key, val)
        minX = max(minCoord, key[0]-dist)
        maxX = min(maxCoord, key[0]+dist)
        for x in range(minX, maxX):
            minY = max(minCoord, key[1]-dist)
            maxY = min(maxCoord, key[1]+dist)
            for y in range(minY, maxY):
                pointDist = manhattanDist(key, (x,y))
                if pointDist <= dist:
                    invalidPoints.add((x,y))
    return invalidPoints

def findBeacon(coords, minCoord, maxCoord):
    allCoords = set()
    for x in range(minCoord, maxCoord):
        for y in range(minCoord, maxCoord):
            allCoords.add((x,y))
    onlyOneCoordSet = allCoords - coords
    if len(onlyOneCoordSet) != 1:
        print('something went wrong')
    return onlyOneCoordSet.pop()

def calcTuningFreq(coord):
    return coord[0]*4000000 + coord[1]

def checkEveryCoord(positions, minC, maxC):
    sensorDists = dict()
    for key, val in positions.items():
        dist = manhattanDist(key, val)
        sensorDists[key] = dist
    for x in range(minC, maxC):
        if x % 1000000 == 0:
            print('x checkpoint')
        for y in range(minC, maxC):
            if y % 1000000 == 0:
                print('y checkpoint')
            badCoord = False
            for key, val in sensorDists.items():
                dist = manhattanDist((x,y), key)
                if dist <= val:
                    badCoord = True
                    break
            if badCoord == False:
                return (x, y)




if __name__ == '__main__':
    with open('day15/input.txt') as f:
        lines = [line.strip() for line in f]
    positions = parseInput(lines)
    # rowOfInterest = 2000000 if len(positions) > 14 else 10
    # invalidPoints = generateRowOfInterestCoords(positions, rowOfInterest)
    # calcPartOne(invalidPoints, rowOfInterest)

    minCoord = 0
    maxCoord = 4000000 if len(positions) > 14 else 20

    coord = checkEveryCoord(positions, minCoord, maxCoord)
    print('tuning frequency is: ' + str(calcTuningFreq(coord)))

