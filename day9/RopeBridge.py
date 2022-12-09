def moveT(knots, tailPositions):
    for i in range(1, len(knots)):
        hx, hy = knots[i-1]
        tx, ty = knots[i]
        if abs(hx - tx) + abs(hy-ty) >= 3: #diag move
            tx += 1 if hx - tx > 0 else -1
            ty += 1 if hy - ty > 0 else -1
        elif abs(hx-tx) == 2: #hor move
            tx += 1 if hx - tx > 0 else -1
        elif abs(hy-ty) == 2: #vert move
            ty += 1 if hy - ty > 0 else -1
        knots[i] = (tx, ty)
    tailPositions.add(knots[-1])

def triggerMoves(x, y, nbrSteps, knots, tailPositions):
    for _ in range(0, nbrSteps):
        hx, hy = knots[0]
        hx += x
        hy += y
        knots[0] = (hx, hy)
        moveT(knots, tailPositions)

def mapMovement(nbrKnots, moves):
    tailPositions = set()
    knots = []
    for _ in range(0, nbrKnots):
        knots.append((0, 0))
    for move in moves:
        if move[0] == 'U':
            triggerMoves(0, 1, int(move[1]), knots, tailPositions)
        elif move[0] == 'D':
            triggerMoves(0, -1, int(move[1]), knots, tailPositions)
        elif move[0] == 'R':
            triggerMoves(1, 0, int(move[1]), knots, tailPositions)
        elif move[0] == 'L':
            triggerMoves(-1, 0, int(move[1]), knots, tailPositions)
    return tailPositions


if __name__ == '__main__':
    with open('day9/input.txt') as f:
        moves = [line.rstrip('\n').split() for line in f]

    print('unique coords visited by tail part1: ' + str(len(mapMovement(2, moves))))
    print('unique coords visited by tail part2: ' + str(len(mapMovement(10, moves))))
