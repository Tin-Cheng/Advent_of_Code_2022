from collections import defaultdict
from collections import deque
import functools
f = open("day16test.txt", "r")
#f = open("day15input.txt", "r")
s = f.read().splitlines()
Gate = defaultdict(bool)
Rate = defaultdict(int)
Tunnels = defaultdict(list)
for str in s:
    A = str.split(' ')
    Gate[A[1]] = False
    Rate[A[1]] = int(A[4].replace(';','').replace('rate=',''))
    Tunnels[A[1]] = [v.replace(',','') for v in A[9:]]

print(Gate)
print(Rate)
print(Tunnels)
REMAINING_TIME = 30
totalgate = len(Gate)
opened = tuple()
for k,v in Rate.items():
    if v==0: opened = opened + (k,)
@functools.lru_cache(maxsize=None)
def part1(loc,Remaining_min,opened) -> int:
    print(loc,Remaining_min,opened)
    if opened == totalgate: return 0
    if Remaining_min <= 0: return 0
    best = 0
    if loc not in opened: 
        openval = (Remaining_min-1) * Rate[loc]
        cur_opened = tuple(sorted(opened + (loc,)))
        for neigh in Tunnels[loc]:
            if openval != 0:
                best = max(best,openval + part1(neigh,Remaining_min-2,cur_opened))
            best = max(best,part1(neigh,Remaining_min,opened))
        

    # for neigh in Tunnels[loc]:
    #     if neigh not in opened:
    #         best = max(best,part1(neigh,Remaining_min-1,opened))
    return best

#print('part1:',part1('AA',REMAINING_TIME,()))
#https://github.com/nthistle/advent-of-code/blob/master/2022/day16/day16.py
def maxflow(cur, opened, min_left):
    if min_left <= 0:
        return 0
    best = 0
    if cur not in opened:
        val = (min_left - 1) * Rate[cur]
        cur_opened = tuple(sorted(opened + (cur,)))
        for adj in Tunnels[cur]:
            if val != 0:
                best = max(best,
                    val + maxflow(adj, cur_opened, min_left - 2))
            best = max(best,
                maxflow(adj, opened, min_left - 1))
    return best

print(maxflow("AA", (), REMAINING_TIME))