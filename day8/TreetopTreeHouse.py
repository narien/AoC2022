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

    left = set(grid[y][0:x])
    if max(left) < myHeight:
        return True

    right = set(grid[y][x+1:len(grid[y])])
    if max(right) < myHeight:
        return True

    up = set()
    for i in range(0, y):
        up.add(grid[i][x])
    if max(up) < myHeight:
        return True

    down = set()
    for i in range(y+1, len(grid)):
        down.add(grid[i][x])
    if max(down) < myHeight:
        return True
    
    return False



def countVisibleTrees(grid):
    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if treeIsVisible(x, y, grid):
                total += 1

    return total

def calcScenicScore(grid):
    maxScore = 0

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            left = 0
            right = 0
            up = 0
            down = 0
            for i in range(x - 1, -1, -1):
                left += 1
                if grid[y][i] >= grid[y][x]:
                    break

            for i in range(x + 1, len(grid[y])):
                right += 1
                if grid[y][i] >= grid[y][x]:
                    break

            for i in range(y - 1, -1, -1):
                up += 1
                if grid[i][x] >= grid[y][x]:
                    break

            for i in range(y + 1, len(grid)):
                down += 1
                if grid[i][x] >= grid[y][x]:
                    break

            total = left*right*up*down
            maxScore = total if total > maxScore else maxScore
    return maxScore

if __name__ == '__main__':
    with open('day8/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    grid = buildGrid(lines)

    print('visible trees: ' + str(countVisibleTrees(grid)))
    print('highest scenic score: ' + str(calcScenicScore(grid)))
