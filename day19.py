from collections import deque
import datetime
#import threading

f = open("day19test.txt", "r")
#f = open("day19input.txt", "r")
s = f.read().splitlines()

Blueprints = []
for line in s:
    A = [int(txt) for txt in line.split() if txt.isdigit()]
    Blueprints.append([int(A[0]),int(A[1]),[int(A[2]),int(A[3])],[int(A[4]),int(A[5])]])

def CheckBuiltable(blueprint,Robots,Resources):
    BuiltRobots,UsedResources = [],[]
    #assume max one per day
    maxResource = [False,False]
    #never create if have enough supply
    maxResource[0] = max(max(blueprint[0],blueprint[1]),max(blueprint[2][0],blueprint[3][0])) == Robots[0]
    maxResource[1] = (blueprint[2][1] == Robots[1]) #or (Resources[1] >= blueprint[2][1] * 2)

    Creatable3 = Resources[0] >= blueprint[3][0] and Resources[2] >= blueprint[3][1]
    if Creatable3:
        BuiltRobots.append([0,0,0,1])
        UsedResources.append([blueprint[3][0],0,blueprint[3][1],0])
        return BuiltRobots,UsedResources

    Creatable2 = Resources[0] >= blueprint[2][0] and Resources[1] >= blueprint[2][1]
    if Creatable2 > 0:
        BuiltRobots.append([0,0,1,0])
        UsedResources.append([blueprint[2][0],blueprint[2][1],0,0])
        return BuiltRobots,UsedResources

    
    if not maxResource[1]:
        if Resources[0] // blueprint[1] > 0:
            BuiltRobots.append([0,1,0,0])
            UsedResources.append([blueprint[1],0,0,0])
    if not maxResource[0]:
        if Resources[0] // blueprint[0] > 0:
            BuiltRobots.append([1,0,0,0])
            UsedResources.append([blueprint[0],0,0,0])
    if len(BuiltRobots) == 0 or Resources[0] < blueprint[0] * 2 or Resources[0] < blueprint[1] * 2:
        BuiltRobots.append([0,0,0,0])
        UsedResources.append([0,0,0,0])
    return BuiltRobots,UsedResources

def Simulation(blueprint,part):
    targetMinutes = 24 if part == 1 else 32
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
        time,Robots,Resources = current
        prev = been.get(time,0)
        if prev > Resources[3] + time * Robots[3] + (time-1)*(time)//2: continue
        been[time] = Resources[3]

        if time == targetMinutes:
            if best < Resources[3]:
                best = Resources[3]
                finalRobots = [r for r in Robots]
                finalResource = [r for r in Resources]
            continue

        BuiltRobots,UsedResources = CheckBuiltable(blueprint,Robots,Resources)
        
        for i,v in enumerate(Robots):
            Resources[i] += v

        for newRobot,UsedResource in zip(BuiltRobots,UsedResources):
            CopyResource = [r for r in Resources]
            for i in range(4):
                newRobot[i] += Robots[i]
                CopyResource[i] -= UsedResource[i]
            q.append([time+1,newRobot,CopyResource])

        for i in range(time+1,targetMinutes+1):
            been[time+i] = max(been.get(time+i,0),Resources[3] + Robots[3] * (i+1))


    print(best,finalRobots,finalResource)
    return best

result1 = 0
for i,blueprint in enumerate(Blueprints):
    print(datetime.datetime.now(),i,Blueprints[i])
    result1 += (i+1) * Simulation(Blueprints[i],1)
print(datetime.datetime.now())
print("part1:",result1)

result2 = 1
for i in range(min(len(Blueprints),3)):
    print(datetime.datetime.now(),i,Blueprints[i])
    result2 *= Simulation(Blueprints[i],2)
print(datetime.datetime.now())
print("part2:",result2)