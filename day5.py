from collections import defaultdict
#f = open("test.txt","r")
f = open("input.txt","r")
stacklines = []
stacks = defaultdict(list)
stacks2 = defaultdict(list)
flag = False
def processStackLines():
    for i in range(len(stacklines)-2,-1,-1):
        s = stacklines[i]
        for j in range(1,len(s),4):
            if s[j] != ' ':
                stacks[j//4+1].append(s[j])
    for key,item in stacks.items():
        stacks2[key] = list(item)

def Move_p1(frm,to,times):
    for _ in range(times):
        stacks[to].append(stacks[frm].pop())

def Move_p2(frm,to,times):
    stacks2[to].extend(stacks2[frm][-times:])
    stacks2[frm] = stacks2[frm][:-times]

for s in f:
    s = s.replace('\n','')
    if flag:
        A = s.split(" ")
        frm,to,times = int(A[3]),int(A[5]),int(A[1])
        Move_p1(frm,to,times)
        Move_p2(frm,to,times)
    elif s == '': 
        flag = True
        processStackLines()
    else:
        stacklines.append(s)

ans = ''
print("Part 1:", "".join(v[-1] for k,v in stacks.items()))
print("Part 2:", "".join(v[-1] for k,v in stacks2.items()))