def executeCommand(line, currentDirs):
    if line[1] == 'cd':
        if line[2] == '/':
            currentDirs = ['/']
        elif line[2] == '..':
            currentDirs.pop()
        else:
            currentDirs.append(line[2])
    return currentDirs
    #elif line[1] == 'ls': # donothing

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
        
        #else: # dir
    return dirSizes

def sumPartOne(dirs):
    total = 0
    for val in dirs.values():
        if val <= 100000:
            total += val
    return total


if __name__ == '__main__':
    with open('day7/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    print(lines)
    dirs = calcSizeInAllDirs(lines)
    print('Sum of dirs for part one: ' + str(sumPartOne(dirs)))
