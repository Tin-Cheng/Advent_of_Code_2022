import time
#test shape: 4x4,3x4
#□□■□
#■■■□
#□□■■
#input shape: 60x60,4x3
#□■■
#□■□
#■■□
#■□□
#f = open("day22test.txt","r")
f = open("day22input.txt", "r")

file = f.read().splitlines()
Map = []
isFirstPart =  True
command = ''
COLS = 0
ROWSBOUND = []
COLSBOUND = []
for line in file:
    if len(line) == 0: isFirstPart =  False
    if isFirstPart:
        Map.append(line)
        leng = len(line)
        ROWSBOUND.append([leng - len(line.lstrip()),leng-1])
        COLS = max(COLS,leng)
    else:
        command = line

ROWS = len(Map)
for i in range(COLS):
    minC,maxC = ROWS,0
    for j in range(ROWS):
        if i < ROWSBOUND[j][0] or i > ROWSBOUND[j][1]: continue
        if Map[j][i] == ' ': continue
        minC = min(minC,j)
        maxC = max(maxC,j)
    COLSBOUND.append([minC,maxC])
    

def Simulation(Map,ROWSBOUND,COLSBOUND,ROWS,COLS,command,part):
    posX,posY,direction = ROWSBOUND[0][0],0,0
    #print('start ',posX,posY)
    distance = 0
    def getFace(posX,posY):
        #only for the input Shape....
        size = 50
        if 0 <= posY < size * 1:
            if size * 1 <= posX < size * 2:
                return 2
            elif size * 2 <= posX < size * 3:
                return 1
            else: assert 'error get face'
        elif size * 1 <= posY < size * 2:
            if size * 1 <= posX < size * 2:
                return 3
            else: assert 'error get face'
        elif size * 2 <= posY < size * 3:
            if 0 <= posX < size * 1:
                return 5
            elif size * 1 <= posX < size * 2:
                return 4
            else: assert 'error get face'
        elif size * 3 <= posY < size * 4:
            if 0 <= posX < size * 1:
                return 6
            else: assert 'error get face'
        else:
            assert 'posY error in get Face'
    def isMovable(posX,posY,direction,part):
        #only for the input Shape....
        size = 50
        #print('isMovable, Y:',posY,';X:',posX,'; direction:',direction,'; face:',face)
        nextX,nextY,newdirection = posX,posY,direction
        if part == 1:
            if direction == 0:
                nextX = ROWSBOUND[posY][0] if posX + 1 > ROWSBOUND[posY][1] else posX + 1
            elif direction == 2:
                nextX = ROWSBOUND[posY][1] if posX - 1 < ROWSBOUND[posY][0] else posX - 1
            elif direction == 1:
                nextY =  COLSBOUND[posX][0] if posY + 1 > COLSBOUND[posX][1] else posY + 1
            elif direction == 3:
                nextY =  COLSBOUND[posX][1] if posY - 1 < COLSBOUND[posX][0] else posY - 1
            if Map[nextY][nextX] != '#': return True,nextX,nextY,direction
            else: return False,posX,posY,direction
            
        elif part == 2:
            if direction == 0:
                if (posX + 1) % size == 0:
                    face = getFace(posX,posY)
                    if face == 1:
                        nextY = size * 3 - posY - 1
                        nextX = size * 2 - 1
                        newdirection = 2
                    elif face == 2:
                        nextX = posX + 1
                    elif face == 3:
                        nextY = size * 1 - 1
                        nextX = size * 1 + posY
                        newdirection = 3
                    elif face == 4:
                        nextY = size * 3 - posY - 1
                        nextX = size * 3 - 1
                        newdirection = 2
                    elif face == 5:
                        nextX = posX + 1
                    elif face == 6:
                        nextY = size * 3 - 1
                        nextX = posY - size * 2
                        newdirection = 3
                else: 
                    nextX = posX + 1
            elif direction == 2:
                if (posX) % size == 0:
                    face = getFace(posX,posY)
                    if face == 1:
                        nextX = posX - 1
                    elif face == 2:
                        nextY = size * 3 - posY - 1
                        nextX = 0
                        newdirection = 0
                    elif face == 3:
                        nextY = size * 2
                        nextX = posY - size
                        newdirection = 1
                    elif face == 4:
                        nextX = posX - 1
                    elif face == 5:
                        nextY = size * 3 - posY - 1
                        nextX = size
                        newdirection = 0
                    elif face == 6:
                        nextY = 0
                        nextX = posY - size * 2
                        newdirection = 1
                else:
                    nextX = posX - 1
            elif direction == 1:
                if (posY + 1) % size == 0:
                    face = getFace(posX,posY)
                    if face == 1:
                        nextY = posX - size
                        nextX = size * 2 - 1
                        newdirection = 2
                    elif face == 2:
                        nextY = posY + 1
                    elif face == 3:
                        nextY = posY + 1
                    elif face == 4:
                        nextY = posX + size * 2
                        nextX = size * 1 - 1
                        newdirection = 2
                    elif face == 5:
                        nextY = posY + 1
                    elif face == 6:
                        nextY = 0
                        nextX = size * 2 + posX
                else:
                    nextY = posY + 1
            elif direction == 3:
                if (posY) % size == 0:
                    face = getFace(posX,posY)
                    if face == 1:
                        nextY = size * 4 - 1
                        nextX = posX - size * 2
                    elif face == 2:
                        nextY = posX + size * 2
                        nextX = 0
                        newdirection = 0
                    elif face == 3:
                        nextY = posY - 1
                    elif face == 4:
                        nextY = posY - 1
                    elif face == 5:
                        nextY = posX + size * 1
                        nextX = size * 1
                        newdirection = 0
                    elif face == 6:
                        nextY = posY - 1
                else:
                    nextY = posY - 1
            if Map[nextY][nextX] != ' ' and Map[nextY][nextX] != '#': 
                #if getFace(posX,posY) != getFace(nextX,nextY): print('from ',getFace(posX,posY) ,'to' ,getFace(nextX,nextY))
                return True,nextX,nextY,newdirection
            else: 
                return False,posX,posY,direction
        else: 
            assert 'error input'
        return posX,posY,direction,part
    def Move(posX,posY,distance,direction, part):
        for _ in range(distance):
            if direction == 0: Map[posY] = Map[posY][:posX] + '>' + Map[posY][posX+1:]
            if direction == 1: Map[posY] = Map[posY][:posX] + 'v' + Map[posY][posX+1:]
            if direction == 2: Map[posY] = Map[posY][:posX] + '<' + Map[posY][posX+1:]
            if direction == 3: Map[posY] = Map[posY][:posX] + '^' + Map[posY][posX+1:]
            movable, posX, posY, direction = isMovable(posX,posY,direction,part)
            #print(posY,posX)
            if Map[posY][posX] == ' ' or Map[posY][posX] == '#': 
                assert 'error'
            if not movable: break
        return posX,posY, direction

    for i,c in enumerate(command):
        if c.isnumeric():
            distance = distance * 10 + int(c)
        else:
            posX,posY,direction = Move(posX,posY,distance,direction, part)
            distance = 0
            if c == "L": direction = (direction-1) % 4
            elif c == "R": direction = (direction+1) % 4
            else: print("invalid command input!", c)
    #final move
    posX,posY, direction = Move(posX,posY,distance,direction, part)

    #for r in Map: print(r)
    return 1000 * (posY+1) + 4 * (posX+1) + direction
start = time.time()
print("part1",Simulation(Map,ROWSBOUND,COLSBOUND,ROWS,COLS,command,1))
middle = time.time()
print("part2",Simulation(Map,ROWSBOUND,COLSBOUND,ROWS,COLS,command,2))
end = time.time()

print(f"Part 1 runs in {middle - start}s")
print(f"Part 2 runs in {end - middle}s")