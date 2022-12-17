import datetime
from collections import defaultdict
from collections import deque
import functools
import heapq
#f = open("day16test.txt", "r")
f = open("day16input.txt", "r")
s = f.read().splitlines()
Rate = defaultdict(int)
Tunnels = defaultdict(list)
length = len(s)
Gate = [""] * length
GateMap = defaultdict(int)
for i,str in enumerate(s):
    A = str.split(' ')
    Gate[i] = A[1]
    GateMap[A[1]] = i
    Rate[A[1]] = int(A[4].replace(';','').replace('rate=',''))
    Tunnels[A[1]] = [v.replace(',','') for v in A[9:]]

#print(Gate)
#print(Rate)
#print(Tunnels)
REMAINING_TIME = 30
@functools.lru_cache(maxsize=None)
def part1(loc,Remaining_min,opened) -> int:
    if Remaining_min <= 1: return 0
    best = 0
    if loc not in opened: 
        openval = (Remaining_min-1) * Rate[loc]
        cur_opened = tuple(sorted(opened + (loc,)))
        for neigh in Tunnels[loc]:
            if openval != 0:
                best = max(best,openval + part1(neigh,Remaining_min-2,cur_opened))
    for neigh in Tunnels[loc]:
        #if neigh not in opened:
        best = max(best,part1(neigh,Remaining_min-1,opened))
    return best

#print('part1:',part1('AA',REMAINING_TIME,()))

ShortestDist = [[float("inf")] * length for _ in range(length)]
Tunnels2 = defaultdict(list)
Rate2 = defaultdict(list)
for k,v in Tunnels.items():
    for t in v:
        Tunnels2[GateMap[k]].append(GateMap[t])
for k,v in Rate.items():
    Rate2[GateMap[k]] = v
#print(Tunnels2)

def makeGraph(i):
    q = [[0,i]]
    been = set()
    while q:
        dis,cur = heapq.heappop(q)
        if cur in been: continue
        been.add(cur)
        ShortestDist[i][cur] = min(ShortestDist[i][cur],dis)
        for nei in Tunnels2[cur]:
            heapq.heappush(q,[dis+1,nei])
for i in range(length):
    makeGraph(i)
#print(ShortestDist)
seen = {}
zeros = ()
for k,v in Rate2.items():
    if v == 0: tuple(sorted(zeros + (k,)))
@functools.lru_cache(maxsize=None)
def part2(loc1,Remaining_min1,loc2,Remaining_min2,opened,score) -> int:
    if Remaining_min1 < 2 or Remaining_min2 < 2: return 0
    if seen.get((loc1,Remaining_min1,loc2,Remaining_min2),-1) >= score: return 0
    seen[(loc1,Remaining_min1,loc2,Remaining_min2)] = score
    best = 0
    openval1 = (Remaining_min1-1) * Rate2[loc1]
    openval2 = (Remaining_min2-1) * Rate2[loc2]
    cur_opened1 = tuple(sorted(opened + (loc1,)))
    cur_opened2 = tuple(sorted(opened + (loc2,)))
    cur_openedboth = tuple(sorted(opened + (loc1,loc2,)))
    #if loc1 > 3 and loc2 > 3: print(loc1,Remaining_min1,loc2,Remaining_min2,openval1,openval2,opened,cur_opened1,cur_opened2)
    #both ok
    if Remaining_min1 == Remaining_min2:
        if loc1 not in opened and Rate2[loc1] > 0: 
            #have to be diff location
            if loc1 != loc2 and loc2 not in opened and Rate2[loc2] > 0: 
                for i,cost1 in enumerate(ShortestDist[loc1]):
                    if i == loc1 or i in opened or Remaining_min1 - cost1 - 1 < 2: continue
                    for j,cost2 in enumerate(ShortestDist[loc2]):
                        if j == loc2 or j in opened or Remaining_min2 - cost2 - 1 < 2: continue
                        #open both
                        best = max(best,openval1 + openval2 + part2(i,Remaining_min1 - cost1 - 1,j,Remaining_min2 - cost2 - 1,cur_openedboth,score + openval1 + openval2))
            else:
                for j,cost2 in enumerate(ShortestDist[loc2]):
                    if j == loc2 or j in opened or Remaining_min2 - cost2 < 2: continue
                    #open 1
                    best = max(best,openval1 + part2(loc1,Remaining_min1 - 1,j,Remaining_min2 - cost2,cur_opened1,score + openval1))
        elif loc2 not in opened and Rate2[loc2] > 0: 
                for i,cost1 in enumerate(ShortestDist[loc1]):
                    if i == loc1 or i in opened or Remaining_min1 - cost1 < 2: continue
                    #open 2
                    best = max(best,openval2 + part2(i,Remaining_min1 - cost1,loc2,Remaining_min2 - 1,cur_opened2,score + openval2))
        #not open for both
        for i,cost1 in enumerate(ShortestDist[loc1]):
            if i == loc1 or i in opened or Remaining_min1 - cost1 < 2: continue
            for j,cost2 in enumerate(ShortestDist[loc2]):
                if j == loc2 or j in opened or Remaining_min2 - cost2 < 2: continue
                #both move on 
                best = max(best,part2(i,Remaining_min1 - cost1,j,Remaining_min2 - cost2,opened,score))
    #1 move
    elif Remaining_min1 > Remaining_min2:
        if loc1 not in opened and Rate2[loc1] > 0:
            best = max(best,openval1 + part2(loc1,Remaining_min1-1,loc2,Remaining_min2,cur_opened1,score + openval1))
        for i,cost1 in enumerate(ShortestDist[loc1]):
            if i == loc1 or Remaining_min1-cost1 < 2: continue
            best = max(best,part2(i,Remaining_min1-cost1,loc2,Remaining_min2,opened,score))
    #2 move
    elif Remaining_min1 < Remaining_min2:
        if loc2 not in opened and Rate2[loc2] > 0:
            best = max(best,openval2 + part2(loc1,Remaining_min1,loc2,Remaining_min2-1,cur_opened2,score + openval2))
        for j,cost2 in enumerate(ShortestDist[loc2]):
            if j == loc2 or Remaining_min2-cost2 < 2: continue
            best = max(best,part2(loc1,Remaining_min1,j,Remaining_min2-cost2,opened,score))
    return best

#print('part2:',part2(GateMap['AA'],REMAINING_TIME - 4,GateMap['AA'],REMAINING_TIME - 4,(),0))
print(datetime.datetime.now())
print('part2:',part2(GateMap['AA'],REMAINING_TIME - 4,GateMap['AA'],REMAINING_TIME - 4,zeros,0))
print(datetime.datetime.now())
#print(GateMap)
#print(Rate)
#print(Rate2)
#print(Tunnels2) 0003