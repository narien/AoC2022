def parseInput(lines):
    nodeGraph = dict()
    for line in lines:
        line = line.split()
        routes = [valve[0:-1] if len(valve) == 3 else valve for valve in line[9:]]
        nodeGraph[line[1]] = (line[4][5:-1], routes)
    return nodeGraph
    
if __name__ == '__main__':
    with open('day16/input.txt') as f:
        lines = [line.strip() for line in f]
    nodeGraph = parseInput(lines)
    
