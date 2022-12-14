from collections import deque
import time
#f = open("day14test.txt", "r")
f = open("day14input.txt", "r")
s = f.read().splitlines()
Lines = []
maxX,maxY = float('-inf'),float('-inf')

for str in s:
    L = str.split(' -> ')
    line = []
    for point in L:
        x,y = point.split(',')
        x,y = int(x),int(y)
        maxX,maxY = max(maxX,x),max(maxY,y)
        line.append([x,y])
    Lines.append(line)
maxX = maxX + 2 + maxY
maxY = maxY + 2
empty = ' '
M = [[empty] * (maxX) for _ in range(maxY)]
for line in Lines:
    lastX,lastY = None, None
    for x,y in line:
        if lastX:
            if lastX == x:
                dy = 1 if y - lastY > 0 else -1
                while lastY != y:
                    lastY += dy
                    M[lastY][x] = '#'
            else:
                dx = 1 if x - lastX > 0 else -1
                while lastX != x:
                    lastX += dx
                    M[y][lastX] = '#'
        M[y][x] = '#'
        lastX,lastY = x,y 
initX = 500
initY = 0
draw = False
def dropSand() -> bool:
    if draw:
        time.sleep(0.3)
        for i in range(20):
            print()
        for m in M:
            print(m[480:520])
    curX = initX
    curY = initY
    while curY < maxY - 1:
        if M[curY + 1][curX] == empty:
            curY += 1
        elif 0 <= curX - 1 and M[curY + 1][curX - 1] == empty:
            curX -= 1
            curY += 1
        elif curX + 1 < maxX and M[curY + 1][curX + 1] == empty:
            curX += 1
            curY += 1
        else: break
    if curY == maxY - 1: return False
    M[curY][curX] = 'O'
    return True

def pourSand() -> int:
    cnt = 0
    q = deque([[initX,initY]])
    while q:
        curX,curY = q.popleft()
        if M[curY][curX] == 'O': continue
        M[curY][curX] = 'O'
        cnt += 1
        if curY == maxY - 1: continue
        if M[curY + 1][curX] == empty: q.append([curX,curY + 1])
        if 0 <= curX - 1 and M[curY + 1][curX - 1] == empty: q.append([curX - 1,curY + 1])
        if curX + 1 < maxX and M[curY + 1][curX + 1] == empty: q.append([curX + 1,curY + 1])
    return cnt
    
def part1():
    cnt = 0
    while dropSand():
        cnt += 1
    print('part1:',cnt)
    return cnt

def part2(p1):
    cnt = pourSand()
    print('part2:',cnt + p1)

p1 = part1()
part2(p1)