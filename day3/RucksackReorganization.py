def getCharVal(char):
    return ord(char) - 38 if char.isupper() else ord(char) - 96

def countCommonItemValue(lines):
    total = 0
    for line in lines:
        compOne, compTwo = line[:len(line)//2], line[len(line)//2:]
        commonItem = ''.join(set(compOne).intersection(compTwo))
        total += getCharVal(commonItem)
    return total

def countBadgeValue(lines):
    total = 0
    for x in range(0, len(lines), 3):
        badge = ''.join(set(lines[x]).intersection(lines[x + 1]).intersection(lines[x + 2]))
        total += getCharVal(badge)
    return total

if __name__ == '__main__':
    with open('day3/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    print('total value of common items is: ' + str(countCommonItemValue(lines)))
    print('total badge value is: ' + str(countBadgeValue(lines)))
