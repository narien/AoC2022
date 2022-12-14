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
    return cave

def sandSettled(cave):
    x = 500
    y = 0

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


def fillWithSand(cave):
    unitsOfSand = 0
    while sandSettled(cave):
        unitsOfSand += 1
    print('units of sand that came to rest: ' + str(unitsOfSand))

if __name__ == '__main__':
    with open('day14/input.txt') as f:
        lines = [line.strip() for line in f]
    caveP1 = buildCaveP1(lines)
    fillWithSand(caveP1)

