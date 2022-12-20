from collections import defaultdict
#f = open("day18test.txt", "r")
f = open("day18input.txt", "r")
s = f.read().splitlines()
Cubes = []
minX,maxX,minY,maxY,minZ,maxZ = float("inf"),float("-inf"),float("inf"),float("-inf"),float("inf"),float("-inf")
for line in s:
    [x,y,z] = line.split(',')
    Cubes.append([int(x),int(y),int(z)])
    minX = min(minX,int(x))
    minY = min(minY,int(y))
    minZ = min(minZ,int(z))
    maxX = max(maxX,int(x))
    maxY = max(maxY,int(y))
    maxZ = max(maxZ,int(z))


#count when create
def part1(Cubes):
    TotalSurface = 0
    AddedCubes = set()
    for x,y,z in Cubes:
        TotalSurface += 6
        AddedCubes.add((x,y,z))
        for dx,dy,dz in [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]:
            newx,newy,newz = x+dx,y+dy,z+dz
            if (newx,newy,newz) in AddedCubes: TotalSurface -= 2
    return TotalSurface
print('part1:',part1(Cubes))

#print(minX,maxX,minY,maxY,minZ,maxZ)
#flooding
def part2(Cubes):
    TotalSurface = 0
    AddedCubes = set()
    Flooded = set()
    for x,y,z in Cubes:
        AddedCubes.add((x,y,z))
    q = [[minX-1,minY-1,minZ-1]]
    while q:
        x,y,z = q.pop()
        if x < minX - 1 or x > maxX + 1 or y < minY - 1 or y > maxY + 1 or z < minZ - 1 or z > maxZ + 1: continue
        if (x,y,z) in Flooded: continue
        Flooded.add((x,y,z))
        for dx,dy,dz in [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]:
            newx,newy,newz = x+dx,y+dy,z+dz
            if (newx,newy,newz) in AddedCubes: TotalSurface += 1
            else: q.append([newx,newy,newz])
    return TotalSurface
print('part2:',part2(Cubes))