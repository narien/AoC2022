
def calcPartOne(opponent, you):
    if opponent == 'A':
        if you == 'X':
            return 4
        elif you == 'Y':
            return 8
        return 3
    if opponent == 'B':
        if you == 'X':
            return 1
        elif you == 'Y':
            return 5
        return 9
    if opponent == 'C':
        if you == 'X':
            return 7
        elif you == 'Y':
            return 2
        return 6

def calcPartTwo(opponent, you):
    if opponent == 'A':
        if you == 'X':
            return 3
        elif you == 'Y':
            return 4
        return 8
    if opponent == 'B':
        if you == 'X':
            return 1
        elif you == 'Y':
            return 5
        return 9
    if opponent == 'C':
        if you == 'X':
            return 2
        elif you == 'Y':
            return 6
        return 7

def calcTotalPartOne(matches):
    totalScore = 0
    for match in matches:
        totalScore += calcPartOne(match[0], match[1])
    return totalScore

def calcTotalPartTwo(matches):
    totalScore = 0
    for match in matches:
        totalScore += calcPartTwo(match[0], match[1])
    return totalScore

if __name__ == '__main__':
    with open('day2/input.txt') as f:
        matches = [val.split() for val in f]
    print('total match score part one: ' + str(calcTotalPartOne(matches)))
    print('total match score part two: ' + str(calcTotalPartTwo(matches)))