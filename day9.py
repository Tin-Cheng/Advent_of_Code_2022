import copy
#f = open("day9test.txt")
#f = open("day9test2.txt")
f = open("day9input.txt")
Lines = f.readlines()
direction = {}
direction['L'] = [-1,0]
direction['R'] = [1,0]
direction['U'] = [0,-1]
direction['D'] = [0,1]
def part1(f):
    H,T = [0,0],[0,0]
    been = set()
    for line in Lines:
        line = line.replace('\n','')
        A = line.split(' ')
        for _ in range(int(A[1])):
            OldH = list(H)
            H[0] += direction[A[0]][0]
            H[1] += direction[A[0]][1]
            dx,dy = H[0] - T[0], H[1] - T[1]
            if abs(dx) == 2 or abs(dy) == 2: T = OldH
            been.add(tuple(T))
        #print(H,T)
    print(len(been))
def part2(f):
    N = [[0,0] for _ in range(10)]
    been = set()
    for line in Lines:
        line = line.replace('\n','')
        A = line.split(' ')
        for x in range(int(A[1])):
            OldN = copy.deepcopy(N)
            N[0][0] += direction[A[0]][0]
            N[0][1] += direction[A[0]][1]
            for i in range(1,10):
                dx,dy = N[i-1][0] - N[i][0], N[i-1][1] - N[i][1]
                if abs(dx) + abs(dy) > 2:
                    N[i][0] += 1 if dx > 0 else -1
                    N[i][1] += 1 if dy > 0 else -1
                elif abs(dx) == 2: 
                    N[i][0] += 1 if dx > 0 else -1
                elif abs(dy) == 2: 
                    N[i][1] += 1 if dy > 0 else -1
            been.add(tuple(N[-1]))
            #print(A,x,N)
    print(len(been))
part1(f)
part2(f)