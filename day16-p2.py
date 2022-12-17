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

#print(Gate)
#print(Rate)
#print(Tunnels)
REMAINING_TIME = 30
#@functools.lru_cache(maxsize=None)
def part2():
    start = ('AA','AA',REMAINING_TIME - 4,(),0,0)
    q = deque([start])
    answer = 0
    seen = {}
    while q:
        now = q.popleft()
        loc1,loc2,Remaining_min,opened,score,flow = now
        if (loc1,loc2,Remaining_min) in seen and seen[(loc1,loc2,Remaining_min)] < score: continue
        seen[(loc1,loc2,Remaining_min)] = score
        if Remaining_min == 0: 
            answer = max(answer,score)
            continue
        if flow == maxflow:
            for i in range(REMAINING_TIME):
                seen[(loc1,loc2,Remaining_min)] = score
                score += flow
            answer = max(answer,score)
            continue

        newflow1 = flow + Rate[loc1]
        newflow2 = flow + Rate[loc2]
        newflowboth = flow + Rate[loc1] + Rate[loc2]
        opened1 = tuple(sorted(opened + (loc1,)))
        opened2 = tuple(sorted(opened + (loc2,)))
        opened_both = tuple(sorted(opened + (loc1,loc2,)))
        #both ok
        if loc1 not in opened and Rate[loc1] > 0: 
            #have to be diff location
            if loc1 != loc2 and loc2 not in opened and Rate[loc2] > 0: 
                #open both
                q.append((neigh1,neigh2,Remaining_min-1,opened_both,score+flow,newflowboth))
            else:
                for neigh2 in Tunnels[loc2]:
                    #open 1
                    q.append((loc1,neigh2,Remaining_min-1,opened1,score+flow,newflow1))
        elif loc2 not in opened and Rate[loc2] > 0: 
                for neigh1 in Tunnels[loc1]:
                    #open 2
                    q.append((neigh1,loc1,Remaining_min-1,opened2,score+flow,newflow2))
        #not open for both
        for neigh1 in Tunnels[loc1]:
            for neigh2 in Tunnels[loc2]:
                #both move on 
                q.append((neigh1,neigh2,Remaining_min-1,opened,score+flow,flow))
    return answer
print(datetime.datetime.now())
print('part2:',part2())
print(datetime.datetime.now())
