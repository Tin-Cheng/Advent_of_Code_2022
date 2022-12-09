f = open("day8input.txt", "r")
#f = open("day8test.txt", "r")
#f = open("day8oth.txt", "r")
M = f.read().split("\n")
M = [[int(val) for val in row] for row in M]
#print(M)
ROWS,COLS = len(M),len(M[0])
M1 = [[False]*COLS for _ in range(ROWS)]
M2 = [[[0,0,0,0]for _ in range(COLS)] for _ in range(ROWS)]
#left to right, right to left, up to down, down to up
#looking left, looking right, looking up, looking down
def part2Search(r,c) -> list[int]:
    res = [0,0,0,0]
    left,right,up,down = 0,0,0,0
    while 0 < left + c:
        res[0] += 1
        left -= 1
        if M[r][left+c] >= M[r][c]:break
    while right + c < COLS - 1:
        res[1] += 1
        right += 1
        if M[r][right+c] >= M[r][c]:break
    while 0 < up + r:
        res[2] += 1
        up -= 1
        if M[up+r][c] >= M[r][c]:break
    while r + down < ROWS - 1:
        res[3] += 1
        down += 1
        if M[down+r][c] >= M[r][c]:break
    return res

for r in range(ROWS):
    curHeight = -1
    curHeightReverse = -1
    stack1 = []
    stack2 = []
    for c in range(COLS):
        if M[r][c] > curHeight:
            curHeight = M[r][c]
            M1[r][c] = True
        colReverse = COLS - c - 1
        if M[r][colReverse] > curHeightReverse:
            curHeightReverse = M[r][colReverse]
            M1[r][colReverse] = True
for c in range(COLS):
    curHeight = -1
    curHeightReverse = -1
    stack1 = []
    stack2 = []
    for r in range(ROWS):
        if M[r][c] > curHeight:
            curHeight = M[r][c]
            M1[r][c] = True
        rowReverse = ROWS - r - 1
        if M[rowReverse][c] > curHeightReverse:
            curHeightReverse =M[rowReverse][c]
            M1[rowReverse][c] = True
for r in range(ROWS):
    for c in range(COLS):
        M2[r][c] = part2Search(r,c)
ans1 = 0
ans2 = 0
for row in M2:
    print(row)
for row in M1:
    ans1 += sum(row)
print(ans1)
for row in M2:
    for col in row:
        cur = 1
        for i in range(4):
            cur *= col[i]
        ans2 = max(ans2,cur)
print(ans2)