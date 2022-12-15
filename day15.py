from collections import deque
#f = open("day15test.txt", "r")
#targetRow,size = 10,20
f = open("day15input.txt", "r")
targetRow,size = 2000000, 4000000
s = f.read().splitlines()
sensor = set()
beacon = set()
lines = []
for str in s:
    A = str.split(' ')
    sensor.add((int(A[2].replace('x=','').replace(',','')),int(A[3].replace('y=','').replace(':',''))))
    beacon.add((int(A[8].replace('x=','').replace(',','')),int(A[9].replace('y=',''))))
    lines.append([int(A[2].replace('x=','').replace(',','')),int(A[3].replace('y=','').replace(':','')),int(A[8].replace('x=','').replace(',','')),int(A[9].replace('y=',''))])
covered = set()
def P1Search(line):
    sx,sy,bx,by = line
    dis = abs(sx-bx) + abs(sy-by)
    if sy - dis <= targetRow <= sy + dis:
        diff = dis - abs(targetRow - sy)
        for i in range(sx-diff,sx+diff+1):
            if (i,targetRow) not in beacon: covered.add(i)
    return
for line in lines:
    P1Search(line)
print('part1:',len(covered))

def P2Search(tr):
    Interval = []
    for line in lines:
        sx,sy,bx,by = line
        dis = abs(sx-bx) + abs(sy-by)
        if sy - dis <= tr <= sy + dis:
            diff = dis - abs(tr - sy)
            lx,rx = max(sx-diff,0),min(sx+diff+1,size)
            Interval.append([lx,rx])
    Interval = merge(Interval)
    if len(Interval) > 1:
        return tr + Interval[0][1] * 4000000
    return -1
    

def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


for i in range(size+1):
    ans = P2Search(i)
    if ans > -1: 
        print('part2:', ans)
        break