import copy
import re

def buildStacks(lines):
    Stacks = [[]]
    tempLines = []

    while True:
        line = lines.pop(0)
        if line[1].isdigit():
            lines.pop(0)
            break
        tempLines.insert(0, line)
    for _ in line.split('   '):
        Stacks.append([])

    for line in tempLines:
        for x in range(1, len(line), 4):
            if line[x].isalpha():
                stackIndex = int(x / 4) + 1 if x > 2 else x
                Stacks[stackIndex].append(line[x])
    return Stacks

def transferContainersPart1(amount, orig, dest, p1Stacks):
    for _ in range(amount):
        box = p1Stacks[orig].pop()
        p1Stacks[dest].append(box)

def transferContainersPart2(amount, orig, dest, p2Stacks):
    stack = []
    for _ in range(amount):
        stack.insert(0, p2Stacks[orig].pop())
    p2Stacks[dest].extend(stack)

def transferContainers(lines, p1Stacks, p2Stacks):
    for line in lines:
        amount, orig, dest = [int(s) for s in re.findall(r'\b\d+\b', line)]
        transferContainersPart1(amount, orig, dest, p1Stacks)
        transferContainersPart2(amount, orig, dest, p2Stacks)

def printTopOfStacks(stacks):
    res = ''
    for stack in stacks:
        if(len(stack)):
            res = res + stack[-1]
    print('top crates: ' + res)

if __name__ == '__main__':
    with open('day5/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    
    p1Stacks = buildStacks(lines)
    p2Stacks = copy.deepcopy(p1Stacks)
    transferContainers(lines, p1Stacks, p2Stacks)

    printTopOfStacks(p1Stacks)
    printTopOfStacks(p2Stacks)
