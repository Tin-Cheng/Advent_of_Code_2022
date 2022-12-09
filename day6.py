from collections import defaultdict
f = open("input.txt","r")
#f = open("test.txt","r")
oa = ord('a')
def find(s:str,n:int)->int:
    l = 0
    been = defaultdict(int)
    for i, c in enumerate(s):
        l = max(l,been[c])
        been[c] = i
        if i == l + n:
            return i + 1
    return -1

for s in f:
    s = s.replace("\n","")
    print(s)
    print("marker: ",find(s,4))
    print("message: ",find(s,14))
