def generate(line):
    first, second = line.split(',')
    fstart, fstop = first.split('-')
    sstart, sstop = second.split('-')

    return set(range(int(fstart), int(fstop) + 1)), set(range(int(sstart), int(sstop) + 1))

def countOverlappingPairs(lines):
    p1 = 0
    p2 = 0
    for line in lines:
        firstArea, secondArea = generate(line)
        if(firstArea.issubset(secondArea) or secondArea.issubset(firstArea)):
            p1 += 1

        if(firstArea.intersection(secondArea)):
            p2 += 1

    return str(p1), str(p2)


if __name__ == '__main__':
    with open('day4/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    
    p1, p2 = countOverlappingPairs(lines)
    print('number of completely overlapping pairs: ' + p1)
    print('number of intersecting pairs: ' + p2)
