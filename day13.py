#f = open("day13test.txt", "r")
f = open("day13input.txt", "r")
s = f.read().splitlines()

def compare(L1,L2):
    for i in range(min(len(L1),len(L2))):
        item1,item2 = L1[i], L2[i]
        #print(item1,item2,type(item1),type(item2))
        if type(item1) is int:
            if type(item2) is int:
                if item1 > item2: return -1
                if item1 < item2: return 1
            else: #type(item2) is list:
                c = compare([item1],item2)
                if c != 0: return c
        else:
            if type(item2) is int:
                c = compare(item1,[item2])
                if c != 0: return c
            else:
                c = compare(item1,item2)
                if c != 0: return c
    if len(L1) == len(L2): return 0
    return 1 if len(L1) < len(L2) else -1

def part1(s):
    ans = 0
    for i in range(0,(len(s)+1)//3):
        if compare(eval(s[i*3]),eval(s[i*3+1])) > 0: ans += (i+1)
    print('part1:',ans)
    
def part2(s):
    A = []
    div1,div1no = '[[2]]',0
    div2,div2no = '[[6]]',0
    s.append(div1)
    s.append(div2)
    for i,item in enumerate(s):
        if item == '': continue
        if not A: A.append(item)
        else:
            l,r = 0, len(A)
            while l < r:
                m = (l+r) // 2
                c = compare(eval(item),eval(A[m]))
                if c > 0: r = m 
                elif c < 0: l = m + 1
            A.insert(l,item)
            if item == div1: div1no = l + 1
            if item == div2: div2no = l + 1
    #print(A)
    print('part2:',div1no, div2no, div1no * div2no)

part1(s)
part2(s)