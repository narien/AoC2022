def executeCommand(line, currentDirs):
    s = ''
    if line[1] == 'cd':
        if line[2] == '/':
            currentDirs = ['/']
        elif line[2] == '..':
            currentDirs.pop()
        else:
            for dir in currentDirs:
                s += dir
            currentDirs.append(s + line[2])
    return currentDirs

def addSize(size, currentDirs, dirSizes):
    for dir in currentDirs:
        if dir in dirSizes:
            dirSizes[dir] += size
        else:
            dirSizes[dir] = size

def calcSizeInAllDirs(lines):
    currentDirs = []
    dirSizes = dict()
    for line in lines:
        line = line.split(' ')
        if line[0] == '$':
            currentDirs = executeCommand(line, currentDirs)
        
        elif line[0].isdigit():
            addSize(int(line[0]), currentDirs, dirSizes)
    return dirSizes

def sumPartOne(dirs):
    total = 0
    for val in dirs.values():
        if val <= 100000:
            total += val
    return total

def sizeOfDirPartTwo(dirs):
    discSize = 70000000
    currentUsed = dirs['/']
    freeSpace = discSize - currentUsed
    extraNeededSpace = 30000000 - freeSpace

    dirSizeToDelete = 70000000
    for val in dirs.values():
        if val >= extraNeededSpace and val < dirSizeToDelete:
            dirSizeToDelete = val
    return dirSizeToDelete


if __name__ == '__main__':
    with open('day7/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    dirs = calcSizeInAllDirs(lines)
    print(dirs)
    print('Sum of dirs for part one: ' + str(sumPartOne(dirs)))
    print('Size of smallest dir to solve part two: ' + str(sizeOfDirPartTwo(dirs)))
