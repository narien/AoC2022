def buildCaveP1(lines):
    xVals = set()
    yVals = set()
    for line in lines:
        vals = line.split(' -> ')
        for val in vals:
            x, y  = val.split(',')
            xVals.add(int(x))
            yVals.add(int(y))

    xMax = max(xVals) + 2
    yMax = max(yVals)  + 2
    cave = [['.'] * xMax for i in range(yMax)]

    for line in lines:
        vals = line.split(' -> ')
        for i in range(len(vals) - 1):
            ix, iy = list(map(int, vals[i].split(',')))
            jx, jy = list(map(int, vals[i+1].split(',')))

            if ix < jx:
                for x in range(ix, jx + 1):
                    cave[iy][x] = '#'
            elif ix > jx:
                for x in range(ix, jx-1, -1):
                    cave[iy][x] = '#'
            elif iy < jy:
                for y in range(iy, jy + 1):
                    cave[y][ix] = '#'
            else:
                for y in range(iy, jy-1, -1):
                    cave[y][ix] = '#'
    return cave, (500, 0)

def buildCaveP2(lines):
    xVals = set()
    yVals = set()
    for line in lines:
        vals = line.split(' -> ')
        for val in vals:
            x, y  = val.split(',')
            xVals.add(int(x))
            yVals.add(int(y))

    xMax = max(xVals) + 2
    yMax = max(yVals)  + 3
    cave = [['.'] * (xMax + 2*yMax) for i in range(yMax)]

    for line in lines:
        vals = line.split(' -> ')
        for i in range(len(vals) - 1):
            ix, iy = list(map(int, vals[i].split(',')))
            jx, jy = list(map(int, vals[i+1].split(',')))

            ix += yMax
            jx += yMax

            if ix < jx:
                for x in range(ix, jx + 1):
                    cave[iy][x] = '#'
            elif ix > jx:
                for x in range(ix, jx-1, -1):
                    cave[iy][x] = '#'
            elif iy < jy:
                for y in range(iy, jy + 1):
                    cave[y][ix] = '#'
            else:
                for y in range(iy, jy-1, -1):
                    cave[y][ix] = '#'

        for x in range(len(cave[0])):
            cave[len(cave)-1][x] = '#'
    return cave, (500+yMax, 0)

def sandSettled(cave, startPoint):
    x, y = startPoint

    while True:
        if y >= len(cave)-1 or x <= 1 or x >= len(cave[y])-1: # falling into void
            return False
        if cave[y+1][x] == '.': # falling
            y += 1
        elif cave[y+1][x-1] == '.': # falling left
            x -= 1
            y += 1
        elif cave[y+1][x+1] == '.': # falling right
            x += 1
            y += 1
        else:
            if cave[y][x] == 'O':
                return False
            cave[y][x] = 'O'
            return True


def fillWithSand(cave, startPoint):
    unitsOfSand = 0
    while sandSettled(cave, startPoint):
        unitsOfSand += 1
    print('units of sand that came to rest: ' + str(unitsOfSand))

def printCave(cave):
    firstRock = 9999999
    for level in cave:
        if '#' in level:
            firstRock = level.index('#') if level.index('#') < firstRock and level.index('#') != 0 else firstRock
    for level in cave:
        print("".join(level[firstRock-1:]))

if __name__ == '__main__':
    with open('day14/input.txt') as f:
        lines = [line.strip() for line in f]
    caveP1, startP1 = buildCaveP1(lines)
    fillWithSand(caveP1, startP1)
    printCave(caveP1)

    caveP2, startP2 = buildCaveP2(lines)
    fillWithSand(caveP2, startP2)
    printCave(caveP2)

