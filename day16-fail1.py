from collections import defaultdict
from collections import deque
import functools
f = open("day16test.txt", "r")
#f = open("day16input.txt", "r")
s = f.read().splitlines()
Gate = defaultdict(bool)
Rate = defaultdict(int)
Tunnels = defaultdict(list)
for str in s:
    A = str.split(' ')
    Gate[A[1]] = False
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


@functools.lru_cache(maxsize=None)
def part2(loc1,avaliable1,loc2,avaliable2,Remaining_min,opened) -> int:
    if Remaining_min <= 0: return 0
    best = 0
    openval1 = (Remaining_min-1) * Rate[loc1]
    openval2 = (Remaining_min-1) * Rate[loc2]
    cur_opened1 = tuple(sorted(opened + (loc1,)))
    cur_opened2 = tuple(sorted(opened + (loc2,)))
    cur_openedboth = tuple(sorted(opened + (loc1,loc2,)))
    #both ok
    if avaliable1 and avaliable2:
        if loc1 not in opened and Rate[loc1] > 0: 
            #have to be diff location
            if loc1 != loc2 and loc2 not in opened and Rate[loc2] > 0: 
                for neigh1 in Tunnels[loc1]:
                    for neigh2 in Tunnels[loc2]:
                        #open both
                        best = max(best,openval1 + openval2 + part2(neigh1,False,neigh2,False,Remaining_min-1,cur_openedboth))
            else:
                for neigh2 in Tunnels[loc2]:
                    #open 1
                    best = max(best,openval1 + part2(loc1,False,neigh2,True,Remaining_min-1,cur_opened1))
        elif loc2 not in opened and Rate[loc2] > 0: 
                for neigh1 in Tunnels[loc1]:
                    #open 2
                    best = max(best,openval2 + part2(neigh1,True,loc1,False,Remaining_min-1,cur_opened2))
        #not open for both
        for neigh1 in Tunnels[loc1]:
            for neigh2 in Tunnels[loc2]:
                #both move on 
                best = max(best,part2(neigh1,True,neigh2,True,Remaining_min-1,opened))
    #1 move
    elif avaliable1:
        if loc1 not in opened and Rate[loc1] > 0:
            #open and readiness turnaround
            best = max(best,openval1 + part2(loc1,False,loc2,True,Remaining_min-1,cur_opened1))
        for neigh1 in Tunnels[loc1]:
            #not open and both ready
            best = max(best,part2(neigh1,True,loc2,True,Remaining_min-1,opened))
    #2 move
    elif avaliable2:
        if loc2 not in opened and Rate[loc2] > 0: 
            #open and readiness turnaround
            best = max(best,openval2 + part2(loc1,True,loc2,False,Remaining_min-1,cur_opened2))
        for neigh2 in Tunnels[loc2]:
            #not open and both ready
            best = max(best,part2(loc1,True,neigh2,True,Remaining_min-1,opened))
    else:
        best = max(best,part2(loc1,True,loc2,True,Remaining_min-1,opened))
    return best

print('part2:',part2('AA',True,'AA',True,REMAINING_TIME - 4,()))