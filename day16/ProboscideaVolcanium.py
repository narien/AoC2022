import copy

def parseInput(lines):
    valveMap = dict()
    for line in lines:
        line = line.split()
        routes = [valve[0:-1] if len(valve) == 3 else valve for valve in line[9:]]
        valveMap[line[1]] = (int(line[4][5:-1]), routes)
    return valveMap

def chooseNextAction(key, valveMap, time, currentFlow, totalFlow):
    print(time)
    newTotalFlow = 0
    valve = valveMap[key]
    for conn in valve[1]:
        newFlow = walkToValve(conn, valveMap, time, currentFlow, totalFlow)
        newTotalFlow = newFlow if newFlow > newTotalFlow else newTotalFlow

    if valve[0] > 0:
        newFlow = turnValve(key, copy.deepcopy(valveMap), time, currentFlow, totalFlow)
        newTotalFlow = newFlow if newFlow > newTotalFlow else newTotalFlow

    return newTotalFlow

def walkToValve(valve, valveMap, time, currentFlow, totalFlow):
    if time == 0:
        return totalFlow
    time -= 1
    totalFlow += currentFlow

    return chooseNextAction(valve, valveMap, time, currentFlow, totalFlow)

def turnValve(key, valveMap, time, currentFlow, totalFlow):
    if time == 0:
        return totalFlow
    time -= 1
    totalFlow += currentFlow

    valve = valveMap[key]
    currentFlow += valve[0]
    valveMap[key] = (0, valve[1])

    return chooseNextAction(key, valveMap, time, currentFlow, totalFlow)

if __name__ == '__main__':
    with open('day16/input.txt') as f:
        lines = [line.strip() for line in f]
    valveMap = parseInput(lines)
    print('most pressure release possible is: ' + str(chooseNextAction('AA', valveMap, 30, 0, 0)))



