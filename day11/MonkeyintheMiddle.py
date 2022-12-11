import copy
import math

class Monkey:
    items = []
    worryEquation = []
    divider = 0
    trueTarget = 0
    falseTarget = 0
    inspectionsDone = 0

    def __init__(self, items, worryEquation, divider, trueTarget, falseTarget):
        self.items = items[:]
        self.worryEquation = worryEquation[:]
        self.divider = divider
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
    
    def operation(self, old):
        p1 = self.worryEquation[0]
        p2 = self.worryEquation[2]
        if self.worryEquation[1] == '*':
            return (int(p1) if p1.isdigit() else old) * (int(p2) if p2.isdigit() else old)
        else:
            return (int(p1) if p1.isdigit() else old) + (int(p2) if p2.isdigit() else old)


def parseInput(lines):
    monkeys = []
    for line in lines:
        match line.split():
            case 'Monkey', i:
                worryEquation = []
                items = []
            case 'Operation:', 'new', '=', s0, s1, s2:
                worryEquation.append(s0)
                worryEquation.append(s1)
                worryEquation.append(s2)
            case 'Test:', 'divisible', 'by', div:
                divider = int(div)
            case 'If', 'true:', 'throw', 'to', 'monkey', target:
                trueTarget = int(target)
            case 'If', 'false:', 'throw', 'to', 'monkey', target:
                falseTarget = int(target)

                trimmedItems = []
                for item in items:
                    item = item[:-1] if item[-1] == ',' else item
                    trimmedItems.append(int(item))
                monkeys.append(Monkey(trimmedItems, worryEquation, divider, trueTarget, falseTarget))
            case myList:
                items = myList[2:]
    return monkeys

def calcMonkeyBusiness(monkeys, iterations, part):
    lcm = math.lcm(*[monkey.divider for monkey in monkeys])

    for _ in range(iterations):
        for monkey in monkeys:
            while(len(monkey.items)):
                oldW = monkey.items.pop(0)
                newW = monkey.operation(oldW)
                if part == 1:
                    newW = int(newW / 3)
                else:
                    newW %= lcm
                monkey.inspectionsDone += 1
                if newW % monkey.divider == 0:
                    monkeys[monkey.trueTarget].items.append(newW)
                else:
                    monkeys[monkey.falseTarget].items.append(newW)

    inspections = [monkey.inspectionsDone for monkey in monkeys]
    inspections.sort()
    topInspectionCounts = inspections[-2:]
    print('monkeybusiness score for part ' + str(part) + ' is: ' + str(topInspectionCounts[0] * topInspectionCounts[1]))

if __name__ == '__main__':
    with open('day11/input.txt') as f:
        lines = [line.strip() for line in f]
    monkeysP1 = parseInput(lines)
    monkeysP2 = copy.deepcopy(monkeysP1)
    calcMonkeyBusiness(monkeysP1, 20, 1)
    calcMonkeyBusiness(monkeysP2, 10000, 2)