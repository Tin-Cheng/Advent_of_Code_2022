import time
from collections import deque
#f = open("day24test.txt","r")
f = open("day24input.txt", "r")

file = f.read().splitlines()
blizzards = set()
for y,line in enumerate(file):
    for x,c in enumerate(line):
        if c == ">":
            blizzards.add((y,x,0))
        elif c == "<":
            blizzards.add((y,x,2))
        elif c == "^":
            blizzards.add((y,x,3))
        elif c == "v":
            blizzards.add((y,x,1))
startY,startX = 0,1
endY,endX = len(file)-1,len(file[0])-2

def SimulationBFS(blizzards,startY,startX,endY,endX,part):
    q = deque([[startY,startX,blizzards,0]])
    def MoveBlizzards(Blizzards):
        newBlizzards = set()
        for y,x,dire in Blizzards:
            if dire == 0:
                x = startX if x == endX else x + 1
                newBlizzards.add((y,x,dire))
            elif dire == 2:
                x = endX if x == startX else x - 1
                newBlizzards.add((y,x,dire))
            elif dire == 1:
                y = startY + 1 if y == endY - 1 else y + 1
                newBlizzards.add((y,x,dire))
            elif dire == 3:
                y = endY - 1 if y == startY + 1 else y - 1
                newBlizzards.add((y,x,dire))
        return newBlizzards
    been = set()
    part2token = 0
    while q:
        curY,curX,curBlizzards,time = q.popleft()
        #print(curY,curX)
        if (curY,curX,time) in been: continue
        been.add((curY,curX,time))
        nextBlizzards = MoveBlizzards(curBlizzards)
        for dy,dx in [[0,1],[0,-1],[1,0],[-1,0],[0,0]]:
            ny, nx = curY + dy, curX + dx
            if ny == endY and nx == endX: 
                if part == 1: return time + 1
                if part == 2 and part2token == 0:
                    q = deque([[ny,nx,nextBlizzards,time+1]])
                    print("end part2 ",part2token, " on ", time + 1)
                    part2token = 1
                    break
                if part == 2 and part2token == 2:
                    print("end part2 ",part2token, " on ", time + 1)
                    return time + 1
            if part2token == 1 and part == 2 and ny == startY and nx == startX: 
                q = deque([[ny,nx,nextBlizzards,time+1]])
                print("end part2 ",part2token, " on ", time + 1)
                part2token = 2
                break
            if ny > endY or ny < startY or nx > endX or nx < startX or (ny == startY and nx != startX) or (ny == endY and nx != endX): continue
            if (ny,nx,0) in nextBlizzards  or (ny,nx,1) in nextBlizzards or (ny,nx,2) in nextBlizzards  or (ny,nx,3) in nextBlizzards: continue
            q.append((ny,nx,nextBlizzards,time+1))
    return -1

#start = time.time()
#print("part1",SimulationBFS(blizzards,startY,startX,endY,endX,1))
middle = time.time()
print("part2",SimulationBFS(blizzards,startY,startX,endY,endX,2))
end = time.time()

#print(f"Part 1 runs in {middle - start}s")
print(f"Part 2 runs in {end - middle}s")
