def buildGrid(lines):
    grid = []
    for line in lines:
        grid.append(line)
    return grid

def treeIsVisible(x, y, grid):
    myHeight = grid[y][x]
    if x == 0 or x == len(grid[0]) - 1:
        return True
    if y == 0 or y == len(grid) - 1:
        return True

    for i in range(0, x):
        print (i)
        # if myHeight <= grid[y][i]:
        #     return False



    for i in range(0, x):
        if myHeight <= grid [y][i]:
            return False
    for i in range(x+1, len(grid[0])):
        if myHeight < grid [y][i]:
            return False
    for i in range(0, y):
        if myHeight < grid [i][x]:
            return False
    for i in range(y+1, len(grid)):
        if myHeight < grid [i][x]:
            return False
    
    return True

    

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
