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
#print(COLS)
    

def part1(Map,ROWSBOUND,COLSBOUND,ROWS,COLS,command):
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    posX,posY,direction = ROWSBOUND[0][0],0,0
    #print('start ',posX,posY)
    commands = []
    distance = 0
    def isMovable(posX,posY,direction):
        nextX,nextY = posX,posY
        if direction == 0:
            nextX = ROWSBOUND[posY][0] if posX + 1 > ROWSBOUND[posY][1] else posX + 1
        elif direction == 2:
            nextX = ROWSBOUND[posY][1] if posX - 1 < ROWSBOUND[posY][0] else posX - 1
        elif direction == 1:
            nextY =  COLSBOUND[posX][0] if posY + 1 > COLSBOUND[posX][1] else posY + 1
        elif direction == 3:
            nextY =  COLSBOUND[posX][1] if posY - 1 < COLSBOUND[posX][0] else posY - 1
        if Map[nextY][nextX] != '#': return True,nextX,nextY
        else: return False,posX,posY

    def Move(posX,posY,distance,direction):
        for _ in range(distance):
            if direction == 0: Map[posY] = Map[posY][:posX] + '>' + Map[posY][posX+1:]
            if direction == 1: Map[posY] = Map[posY][:posX] + 'v' + Map[posY][posX+1:]
            if direction == 2: Map[posY] = Map[posY][:posX] + '<' + Map[posY][posX+1:]
            if direction == 3: Map[posY] = Map[posY][:posX] + '^' + Map[posY][posX+1:]
            movable, posX, posY = isMovable(posX,posY,direction)
            if Map[posY][posX] == ' ': assert 'error'
            if not movable:
                break
        return posX,posY
    for i,c in enumerate(command):
        if c.isnumeric():
            distance = distance * 10 + int(c)
        else:
            commands.append(distance)
            commands.append(c)
            posX,posY = Move(posX,posY,distance,direction)
            #print(direction,distance,posY,posX,c)
            distance = 0
            if c == "L": direction = (direction-1) % 4
            elif c == "R": direction = (direction+1) % 4
            else: print("invalid command input!", c)
    #final move
    print('finalmove',direction,distance,posY,posX,c)
    posX,posY = Move(posX,posY,distance,direction)
    #print(commands)
    for r in Map: print(r)
    return 1000 * (posY+1) + 4 * (posX+1) + direction
print("part1",part1(Map,ROWSBOUND,COLSBOUND,ROWS,COLS,command))



#for r in Map:
#    print(r,len(r))
#print(command)
#print(ROWSBOUND)
#print(COLSBOUND)
#print(ROWS,COLS)

#for i,r in enumerate(Map):
    #print(r[ROWSBOUND[i][0]:ROWSBOUND[i][1]])