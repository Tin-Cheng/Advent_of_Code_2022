from collections import defaultdict
f = open("input.txt","r")
#f = open("test.txt","r")
#root = defaultdict(lambda: defaultdict(int))
root = defaultdict(int)
stack = []
for index,s in enumerate(f):
    s = s.replace("\n","")
    A = s.split(" ")
    #print(A)
    match A:
        case["$","cd","/"]:
            stack = []
        case["$","cd",".."]:
            stack.pop()
        case["$","cd",dir]:
            stack.append(dir)
        case["$","ls"]:
            continue
        case["dir",dir]:
            continue
        case[size,file]:
            for i in range(len(stack)+1):
                #print(i,stack,['']+stack[:i])
                root["/".join(['']+stack[:i])] += int(size)
            
            #print(index,size,file,stack,root)
print(root)
total = 0
p2 = 70000000
available = 70000000
required = 30000000
used = root['']
minimumToBeFree = required + used - available
print(minimumToBeFree)
for k,v in root.items():
    if v < 100000: total += v
    if v >= minimumToBeFree: p2 = min(p2,v)
print("p1: ", total)
print("p2: ", p2)
