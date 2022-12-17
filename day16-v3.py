from collections import defaultdict
from collections import deque
import functools
import datetime
f = open("day16test.txt", "r")
#f = open("day16input.txt", "r")
s = f.read().splitlines()
Gate = defaultdict(bool)
Rate = defaultdict(int)
Tunnels = defaultdict(list)
maxflow = 0
for str in s:
    A = str.split(' ')
    Gate[A[1]] = False
    Rate[A[1]] = int(A[4].replace(';','').replace('rate=',''))
    maxflow += Rate[A[1]] 
    Tunnels[A[1]] = [v.replace(',','') for v in A[9:]]
REMAINING_TIME = 26
@functools.lru_cache(maxsize=None)
def part2(score,loc1,loc2,Remaining_min,opened):
    if Remaining_min == 0: 
        return score
    flow = sum(Rate[v] for v in opened)
    if flow == maxflow:
        return part2(score,loc1,loc2,Remaining_min-1,opened)

    newflow1 = flow + Rate[loc1]
    newflow2 = flow + Rate[loc2]
    newflowboth = flow + Rate[loc1] + Rate[loc2]
    opened1 = tuple(sorted(opened + (loc1,)))
    opened2 = tuple(sorted(opened + (loc2,)))
    opened_both = tuple(sorted(opened + (loc1,loc2,)))
    newscore = score + flow
    #both ok
    best = 0
    
    if loc1 not in opened and Rate[loc1] > 0: 
        #have to be diff location
        if loc1 != loc2 and loc2 not in opened and Rate[loc2] > 0: 
            #open both
            best = max(best,part2(newscore,loc1,loc2,Remaining_min-1,opened_both))
        else:
            for neigh2 in Tunnels[loc2]:
                #open 1
                best = max(best,part2(newscore,loc1,neigh2,Remaining_min-1,opened1))
    elif loc2 not in opened and Rate[loc2] > 0: 
            for neigh1 in Tunnels[loc1]:
                #open 2
                best = max(best,part2(newscore,neigh1,loc2,Remaining_min-1,opened2))
    else:
        #not open for both
        for neigh1 in Tunnels[loc1]:
            for neigh2 in Tunnels[loc2]:
                #both move on 
                best = max(best,part2(newscore,neigh1,neigh2,Remaining_min-1,opened))
    return best
print(datetime.datetime.now())
print('part2:',part2(0,'AA','AA',REMAINING_TIME,()))
print(datetime.datetime.now())
