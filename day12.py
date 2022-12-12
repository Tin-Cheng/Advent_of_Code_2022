from collections import deque
from copy import deepcopy
#f = open("day12test.txt", "r")
f = open("day12input.txt", "r")
s = f.read().splitlines()
RowCnt = len(s)
ColCnt = len(s[0]) 
start = end = [0,0]
M = [[0] * ColCnt for _ in range(RowCnt)]
oa = ord('a')
Starts = []
for r,row in enumerate(s):
    for c,v in enumerate(row):
        if v == 'S':
            start = [r,c]
            M[r][c] = 0
            Starts.append([r,c])
        elif v == 'E':
            end = [r,c]
            M[r][c] = 25
        elif v == 'a':
            M[r][c] = 0
            Starts.append([r,c])
        else:
            M[r][c] = ord(v) - oa
def dfs(tempM,starts):
    M = deepcopy(tempM)
    q = deque([])
    for row,col in starts:
        q.append([row,col,0])
    ans = float("inf")
    while q:
        curRow,curCol,step = q.popleft()
        if curRow == end[0] and curCol == end[1]: 
            ans = min(ans,step)
            continue
        if M[curRow][curCol] > 25: continue
        curHeight = M[curRow][curCol]
        M[curRow][curCol] = 26
        for dr,dc in [[-1,0],[1,0],[0,-1,],[0,1]]:
            newRow,newCol = curRow + dr, curCol + dc
            if 0 <= newRow < RowCnt and 0 <= newCol < ColCnt:
                if M[newRow][newCol] <= curHeight + 1:
                    q.append([newRow,newCol,step+1])
    print(ans)

print("part1:")
dfs(M,[start])
print("part2:")
dfs(M,Starts)
