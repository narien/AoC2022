import re

def buildStacks(lines):
    stacks = [[]]
    tempLines = []

    while True:
        line = lines.pop(0)
        if line[1].isdigit():
            lines.pop(0)
            break
        tempLines.insert(0, line)
    for _ in line.split('   '):
        stacks.append([])

    for line in tempLines:
        for x in range(1, len(line), 4):
            if line[x].isalpha():
                stackIndex = int(x / 4) + 1 if x > 2 else x
                stacks[stackIndex].append(line[x])
    return stacks

def transferContainersPart1(lines, stacks):
    for line in lines:
        amount, orig, dest = re.findall(r'\d+', line)
        for _ in range(int(amount)):
            box = stacks[int(orig)].pop()
            stacks[int(dest)].append(box)

def transferContainersPart2(lines, stacks):
    for line in lines:
        amount, orig, dest = re.findall(r'\d+', line)
        stack = []
        for _ in range(int(amount)):
            stack.insert(0, stacks[int(orig)].pop())
        print(stacks)
        stacks[int(dest)].extend(stack)

if __name__ == '__main__':
    with open('day5/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    
    stacks = buildStacks(lines)
    transferContainersPart1(lines, stacks)

    res = ''
    for stack in stacks:
        if(len(stack)):
            res = res + stack[-1]
    print(res)

    with open('day5/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    
    stacks = buildStacks(lines)
    transferContainersPart2(lines, stacks)

    res = ''
    for stack in stacks:
        if(len(stack)):
            res = res + stack[-1]
    print(res)
