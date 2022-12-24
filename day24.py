import time
from collections import deque
#f = open("day24test.txt","r")
f = open("day24input.txt", "r")
file = f.read().splitlines()

BlizzardsY,BlizzardsX = set(), set()
startY,startX = 0,1
endY,endX = len(file)-1,len(file[0])-2
height, width = endY - startY - 1, endX - startX + 1

for y,line in enumerate(file):
    for x,c in enumerate(line):
        if c == ">":
            for dx in range(width):
                BlizzardsX.add((y,x + dx - (width if x + dx > endX else 0),dx))
        elif c == "<":
            for dx in range(width):
                BlizzardsX.add((y,x - dx + (width if x - dx < startX else 0),dx))
        elif c == "^":
            for dy in range(height):
                BlizzardsY.add((y - dy + (height if y - dy <= startY else 0),x,dy))
        elif c == "v":
            for dy in range(height):
                BlizzardsY.add((y + dy - (height if y + dy >= endY else 0),x,dy))

def SimulationBFS(BlizzardsY,BlizzardsX,startY,startX,endY,endX,part):
    q = deque([[startY,startX,0]])
    been = set()
    part2token = 0
    while q:
        curY,curX,time = q.popleft()
        time = time + 1
        if (curY,curX,time) in been: continue
        been.add((curY,curX,time))
        for dy,dx in [[0,1],[0,-1],[1,0],[-1,0],[0,0]]:
            ny, nx = curY + dy, curX + dx
            if ny == endY and nx == endX: 
                if part == 1: return time
                if part == 2 and part2token == 0:
                    q = deque([[ny,nx,time]])
                    print("end part2 ",part2token, " on ", time)
                    part2token = 1
                    break
                if part == 2 and part2token == 2:
                    print("end part2 ",part2token, " on ", time)
                    return time
            if ny == startY and nx == startX and part2token == 1 and part == 2:
                q = deque([[ny,nx,time]])
                print("end part2 ",part2token, " on ", time)
                part2token = 2
                break
            if ny > endY or ny < startY or nx > endX or nx < startX or (ny == startY and nx != startX) or (ny == endY and nx != endX): continue
            if(ny,nx,(time) % width) in BlizzardsX or (ny,nx,(time) % height) in BlizzardsY: continue
            q.append((ny,nx,time))
    return -1

start = time.time()
print("part1",SimulationBFS(BlizzardsY,BlizzardsX,startY,startX,endY,endX,1))
middle = time.time()
print("part2",SimulationBFS(BlizzardsY,BlizzardsX,startY,startX,endY,endX,2))
end = time.time()

print(f"Part 1 runs in {middle - start}s")
print(f"Part 2 runs in {end - middle}s")