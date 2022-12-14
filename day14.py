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
def dropSand(x,y) -> list[int,bool]:
    if y == maxY - 1: return [0,False]
    if x < 0 or x == maxX: return [0,False]
    if M[y][x] != empty: return [0,True]
    left, down, right = [0,False], [0,False], [0,False]
    down = dropSand(x,y+1)
    if down[1]:
        left = dropSand(x-1,y+1)
    if left[1]:
        right = dropSand(x+1,y+1)
    if left[1] and down[1] and right[1]:
        M[y][x] = 'O'
        return [left[0] + down[0] + right[0] + 1,True]
    return [left[0] + down[0] + right[0],False]

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
    cnt = dropSand(initX,initY)[0]
    print('part1:',cnt)
    return cnt

def part2(p1):
    cnt = pourSand()
    print('part2:',cnt + p1)

p1 = part1()
part2(p1)