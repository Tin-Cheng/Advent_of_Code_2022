from collections import deque
import datetime
f = open("day19test.txt", "r")
#f = open("day19input.txt", "r")
s = f.read().splitlines()

Blueprints = []
for line in s:
    A = (line.replace("Blueprint ","")
    .replace(": Each ore robot costs","")
    .replace(" ore. Each clay robot costs","")
    .replace(" ore. Each obsidian robot costs","")
    .replace(" ore and","")
    .replace(" ore and","")
    .replace(" clay. Each geode robot costs","")
    .replace(" ore and ","")
    .replace(" obsidian.","")
    .split(" ")
    )
    Blueprints.append([int(A[1]),int(A[2]),[int(A[3]),int(A[4])],[int(A[5]),int(A[6])]])

def CheckBuiltable(remainTime,blueprint,Robots,Resources):
    BuiltRobots,UsedResources = [[0,0,0,0]],[[0,0,0,0]]
    if remainTime == 0: 
        return BuiltRobots,UsedResources
    #assume max one per day
    maxResource = [0,0,0]
    maxResource[0] = (blueprint[3][0] * (Robots[3]+1) + blueprint[2][0] * (Robots[2]+1)) // (Robots[0] + 1) + 1
    maxResource[1] = (blueprint[2][1] * (Robots[2]+1) // (Robots[1]+1)) + 1
    maxResource[2] = (blueprint[3][1] * (Robots[3]+1) // (Robots[2]+1)) + 1
    been = set()
    been.add("0,0,0,0")
    #for i in range(4):
    for i in [2,3]:
        curResource = [r for r in Resources]
        curRobots = [0,0,0,0]
        usedResource = [0,0,0,0]
        for j in range(4):
            k = (i+j) % 4
            if k <= 1:
                if k == 0 and Resources[0] >= maxResource[0]: continue
                if k == 1 and Resources[1] >= maxResource[1]: continue
                Creatable = curResource[0] // blueprint[k]
                curRobots[k] += Creatable
                curResource[0] -= Creatable * blueprint[k]
                usedResource[0] += Creatable * blueprint[k]
            elif k == 2:
                if Resources[2] >= maxResource[2]: continue
                Creatable = min(curResource[0] // blueprint[k][0],curResource[1] // blueprint[k][1])
                curRobots[k] += Creatable
                curResource[0] -= Creatable * blueprint[k][0]
                curResource[1] -= Creatable * blueprint[k][1]
                usedResource[0] += Creatable * blueprint[k][0]
                usedResource[1] += Creatable * blueprint[k][1]
            elif k == 3:
                Creatable = min(curResource[0] // blueprint[k][0],curResource[2] // blueprint[k][1])
                curRobots[k] += Creatable
                curResource[0] -= Creatable * blueprint[k][0]
                curResource[2] -= Creatable * blueprint[k][1]
                usedResource[0] += Creatable * blueprint[k][0]
                usedResource[2] += Creatable * blueprint[k][1]
        check = ",".join([str(r) for r in curRobots])
        if check not in been:
            BuiltRobots.append(curRobots)
            UsedResources.append(usedResource)
            been.add(check)
    return BuiltRobots,UsedResources

def Part1Simulation(blueprint):
    targetMinutes = 24
    #ore,clay,obsidian,geode
    StartRobots = [1,0,0,0]
    StartResources = [0,0,0,0]
    best = 0
    finalRobots = StartRobots
    finalResource = StartResources
    q = [(0,StartRobots,StartResources)]
    been = {}
    while q:
        current = q.pop()
        #print(current)
        time,Robots,Resources = current
        beenRobots = ",".join([str(r) for r in Robots])
        beenResources = ",".join([str(r) for r in Resources])
        prev = been.get((time, beenRobots, beenResources), [[-1,-1,-1,-1],[-1,-1,-1,-1]])
        #if prev[0][2] >= Robots[2] and prev[0][3] >= Robots[3] and prev[1][2] >=Resources[2] and prev[1][3] >=Resources[3]:
        #    continue

        been[(time, beenRobots, beenResources)] = [Robots,Resources]

        if time == targetMinutes:
            if best < Resources[3]:
                best = Resources[3]
                finalRobots = [r for r in Robots]
                finalResource = [r for r in Resources]
            #print(current)
            continue

        BuiltRobots,UsedResources = CheckBuiltable(targetMinutes-time,blueprint,Robots,Resources)
        
        for i,v in enumerate(Robots):
            Resources[i] += v
        for newRobot,UsedResource in zip(BuiltRobots,UsedResources):
            CopyResource = [r for r in Resources]
            for i in range(4):
                newRobot[i] += Robots[i]
                CopyResource[i] -= UsedResource[i]
            #print('append',time+1,newRobot,CopyResource)
            q.append([time+1,newRobot,CopyResource])
    print(best,finalRobots,finalResource)
    return best
p1 = 0
for i,blueprint in enumerate(Blueprints):
    print(datetime.datetime.now(),i,blueprint)
    ans = Part1Simulation(blueprint)
    p1 += (i+1) * ans
    print(i,ans)
print(datetime.datetime.now())
print("part1:",p1)