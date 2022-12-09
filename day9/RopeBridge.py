def moveT(hx, hy, tx, ty):
    if abs(hx - tx) + abs(hy-ty) == 3: #diag move
        tx += 1 if hx - tx > 0 else -1 
        ty += 1 if hy - ty > 0 else -1 
        
    elif abs(hx-tx) == 2: #hor move
        tx += 1 if hx - tx > 0 else -1 
    elif abs(hy-ty) == 2: #vert move
        ty += 1 if hy - ty > 0 else -1 
    return tx, ty

def moveUp(nbrSteps, hx, hy, tx, ty, tailPositions):
    for _ in range(0, nbrSteps):
        hy +=1
        tx, ty = moveT(hx, hy, tx, ty)
        tailPositions.add((tx, ty))
    return hx, hy, tx, ty

def moveDown(nbrSteps, hx, hy, tx, ty, tailPositions):
    for _ in range(0, nbrSteps):
        hy -=1
        tx, ty = moveT(hx, hy, tx, ty)
        tailPositions.add((tx, ty))
    return hx, hy, tx, ty

def moveRight(nbrSteps, hx, hy, tx, ty, tailPositions):
    for _ in range(0, nbrSteps):
        hx +=1
        tx, ty = moveT(hx, hy, tx, ty)
        tailPositions.add((tx, ty))
    return hx, hy, tx, ty

def moveLeft(nbrSteps, hx, hy, tx, ty, tailPositions):
    for _ in range(0, nbrSteps):
        hx -=1
        tx, ty = moveT(hx, hy, tx, ty)
        tailPositions.add((tx, ty))
    return hx, hy, tx, ty

def mapMovement(moves):
    tailPositions = set()
    hx = 0
    hy = 0
    tx = 0
    ty = 0
    for move in moves:
        if move[0] == 'U':
            hx, hy, tx, ty = moveUp(int(move[1]), hx, hy, tx, ty, tailPositions)
        elif move[0] == 'D':
            hx, hy, tx, ty = moveDown(int(move[1]), hx, hy, tx, ty, tailPositions)
        elif move[0] == 'R':
                hx, hy, tx, ty = moveRight(int(move[1]), hx, hy, tx, ty, tailPositions)
        elif move[0] == 'L':
                hx, hy, tx, ty = moveLeft(int(move[1]), hx, hy, tx, ty, tailPositions)
    return tailPositions


if __name__ == '__main__':
    with open('day9/input.txt') as f:
        moves = [line.rstrip('\n').split() for line in f]

    print('unique coords visited by tail: ' + str(len(mapMovement(moves))))
