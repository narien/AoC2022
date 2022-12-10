signalIntervals = [20, 60, 100, 140, 180, 220]
signals = set()
drawIntervals = [40, 80, 120, 160, 200, 240]
drawLine = []

def draw(cycles, regX):
    currentPixel = (cycles % 40) - 1
    if currentPixel >= regX - 1 and currentPixel <= regX + 1:
        drawLine.append('#')
    else:
        drawLine.append('.')
    if cycles in drawIntervals:
        print("".join(drawLine))
        drawLine.clear()

def waitCycle(cycles, regX):
    cycles += 1
    draw(cycles, regX)
    if cycles in signalIntervals:
        signals.add(cycles*regX)
    return cycles

def updateCycle(cycles, regX, xUpdate):
    cycles += 1
    draw(cycles, regX)
    if cycles in signalIntervals:
        signals.add(cycles*regX)
    regX += xUpdate
    return cycles, regX

def runProgram(lines):
    cycles = 0
    regX = 1
    
    for line in lines:
        match line.split():
            case ['noop']:
                cycles = waitCycle(cycles, regX)
            case 'addx', xUpdate:
                cycles = waitCycle(cycles, regX)
                cycles, regX = updateCycle(cycles, regX, int(xUpdate))

if __name__ == '__main__':
    with open('day10/input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    runProgram(lines)
    print('sum of signal strengths: ' + str(sum(signals)))