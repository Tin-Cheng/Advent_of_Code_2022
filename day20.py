#f = open("day20test.txt", "r")
f = open("day20input.txt", "r")
file = f.read().splitlines()
Ori = []
for i,line in enumerate(file):
    Ori.append(int(line))
def Mix(Ori,part):
    KEY = 811589153
    dict = {}
    leng = len(file)
    S = []
    for i,line in enumerate(Ori):
        dict[i] = int(line) * (KEY if part == 2 else 1)
        S.append(int(line))
    A = [i for i in range(leng)]
    times = 10 if part == 2 else 1
    for _ in range(times):
        for i in range(leng):
            index = A.index(i)
            A.pop(index)
            newindex = (index + dict[i])
            newindex = (newindex) % (leng-1) 
            #always put at the end
            newindex += leng - 1 if newindex == 0 else 0 
            A.insert(newindex,i)
    ResultA = [dict[num] for num in A]
    indexZero = ResultA.index(0)
    result = []
    for i in [1000,2000,3000]:
        result.append(ResultA[(indexZero+i)%leng])
    return sum(result)
print("part1:", Mix(Ori,1))
print("part2:", Mix(Ori,2))
    