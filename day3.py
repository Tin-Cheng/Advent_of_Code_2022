#f = open("input.txt", "r")
f = open("test.txt", "r")
oa, oz, oA, oZ = ord('a'),ord('z'),ord('A'),ord('Z')
total1 = 0
total2 = 0
def getScore(c):
    oc = ord(c)
    if oa <= oc <= oz:
        return oc-oa + 1
    else:
        return oc-oA + 27
    return 0
def getPriorites(s1,s2):
    for c in s1:
        if c in s2:
            return getScore(c)
    return 0
def getBadges(A):
    exist = set()
    for c in A[0]:
        if c in A[1]:
            exist.add(c)
    for c in exist:
        if c in A[2]:
            return getScore(c)
    return 0 

i = 0
cur = []
for s in f:
    s = s.replace('\n','')
    #part1
    half  = len(s) // 2
    s1,s2 = s[:half],s[half:]
    total1 += getPriorites(s1,s2)
    #part2
    cur.append(s)
    if i == 2:
        i -= 3
        total2 += getBadges(cur)
        cur = []
    i += 1
print(total1)
print(total2)