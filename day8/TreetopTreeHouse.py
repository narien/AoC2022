def buildGrid(lines):
    grid = []
    currLine = 0
    for line in lines:
        grid.append([])
        for char in line:
            grid[currLine].append(int(char))
        currLine += 1
    return grid

def treeIsVisible(x, y, grid):
    myHeight = int(grid[y][x])
    if x == 0 or x == len(grid[0]) - 1:
        return True
    if y == 0 or y == len(grid) - 1:
        return True

    lh = set(grid[y][0:x])
    if max(lh) < myHeight:
        return True

    rh = set(grid[y][x+1:len(grid[y])])
    if max(rh) < myHeight:
        return True

    tv = set()
    for i in range(0, y):
        tv.add(grid[i][x])
    if max(tv) < myHeight:
        return True

    bv = set()
    for i in range(y+1, len(grid)):
        bv.add(grid[i][x])
    if max(bv) < myHeight:
        return True
    
    return False



def countVisibleTrees(grid):
    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if treeIsVisible(x, y, grid):
                total += 1

    return total

if __name__ == '__main__':
    with open('day8/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    grid = buildGrid(lines)

    print('visible trees: ' + str(countVisibleTrees(grid)))
