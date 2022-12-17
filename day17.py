#f = open("day17test.txt", "r")
f = open("day17input.txt", "r")
Jet = f.read().splitlines()[0]

WIDE = 7
DLEFT = 2
DTOP = 3
MMAX = 90

A = [["#","#","#","#"]]
B = [[".","#","."],["#","#","#"],[".","#","."]]
C = [[".",".","#"],[".",".","#"],["#","#","#"]]
D = [["#"],["#"],["#"],["#"]]
E = [["#","#"],["#","#"]]
Rocks = [A,B,C,D,E]
RocksHeight = [1,3,3,4,2]
RocksWidth = [4,3,3,1,2]

def Simulation(part,Jet,Rocks,RocksHeight,RocksWidth):
    M = [["."] * WIDE for _ in range(MMAX)]
    def printM():
        for i in range(len(M)-1,-1,-1):
            print(M[i])
    height = 0
    JetLength = len(Jet)
    JetIndex = 0
    def FixRock(type,x,y):
        for i,row in enumerate(Rocks[type]):
            for j,v in enumerate(row):
                if v == "#":
                    M[y-i][x+j] = "#" 

    def CheckCollision(type,x,y):
        for i,row in enumerate(Rocks[type]):
            for j,v in enumerate(row):
                if M[y-i][x+j] == '#' and v == '#': return False
        return True

    #0 left, 1 right, 2 down
    def MoveRock(type,x,y,dire):
        if dire == 0:
            if x == 0: return x,y,False
            if CheckCollision(type,x-1,y): return (x-1,y,True)
            else: return (x,y,False)
        elif dire == 1:
            if x + RocksWidth[type] >= WIDE: return x,y,False
            if CheckCollision(type,x+1,y): return (x+1,y,True)
            else: return (x,y,False)
        elif dire == 2:
            if y - RocksHeight[type] < 0: return (x,y,False)
            if CheckCollision(type,x,y-1): return (x,y-1,True)
            else: return (x,y,False)

    def dropRock(type,JetLength,JetIndex,height):
        x,y = DLEFT, height + 2 + RocksHeight[type]
        downFlag = True
        while downFlag:
            dire = 1 if Jet[JetIndex] == '>' else 0
            x,y,_ = MoveRock(type,x,y,dire)
            JetIndex = (JetIndex + 1) % JetLength
            x,y,downFlag = MoveRock(type,x,y,2)
        FixRock(type,x,y)
        return (JetIndex,max(height,y+1))
    
    rang = 2022 if part == 1 else 1000000000000
    
    seen = {}
    exheight = 0
    remainrange = 0
    startfrom = 0
    removedRows = 0
    for i in range(rang):
        matrix = ""
        for row in M:
            matrix += "".join(row)

        if  (i%5,JetIndex,matrix) in seen:
            #print('seen',i,i%5,JetIndex)
            #print('olddata',seen[(i%5,JetIndex,matrix)])
            oldDrops,oldHeight = seen[(i%5,JetIndex,matrix)]
            dropsInCycle = (i - oldDrops)
            remainrange = (rang - i + 1) % dropsInCycle
            exheight = (rang - i + 1) // dropsInCycle * (height + removedRows - oldHeight)
            startfrom = i
            print('check ','cur:',i,'; olddrops:',oldDrops,'; new height:',height + removedRows,'; oldheight:',oldHeight,'; cycle:',dropsInCycle,'; remain:',remainrange)
            break
        seen[(i%5,JetIndex,matrix)] = [i,height + removedRows]

        JetIndex,height = dropRock(i%5,JetLength,JetIndex,height)
        while height > MMAX - 10:
            M.append(["."] * WIDE)
            M.pop(0)
            height -= 1
            removedRows += 1

    for i in range(remainrange-1):
        JetIndex,height = dropRock((startfrom+i)%5,JetLength,JetIndex,height)
        while height > MMAX - 10:
            M.append(["."] * WIDE)
            M.pop(0)
            height -= 1
            removedRows += 1
    #print('return:',height, removedRows, exheight)
    return height + exheight + removedRows

print("part1:",Simulation(1,Jet,Rocks,RocksHeight,RocksWidth))
print('matrix max height:', MMAX)
print("part2:",Simulation(2,Jet,Rocks,RocksHeight,RocksWidth))
