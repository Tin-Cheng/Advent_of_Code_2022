import time
#f = open("day25test.txt","r")
f = open("day25input.txt", "r")
file = f.read().splitlines()
def parseFile(input,part):
    d = {'0':0,'1':1,'2':2,'-':-1,'=':-2}
    revd = {0:'0',1:'1',2:'2',-1:'-',-2:'='}
    total = 0
    for line in input:
        amt = 0
        for c in line:
            amt = amt * 5 + d[c]
        total += amt
    p = 0
    while 2 * pow(5,p) < total:
        p += 1
    stack = []
    while p >= 0:
        amt = total // pow(5,p)
        total -= amt * pow(5,p)
        p -= 1
        stack.append(amt)
    ans = ''
    carry = 0
    while stack:
        c = stack.pop()
        if carry + c > 2:
            cur = (c + carry) % 5
            carry = (c + carry) // 5
            if cur > 2:
                carry += 1
                cur -= 5
            ans = revd[cur] + ans
        else:
            ans = revd[c + carry] + ans
            carry = 0
    
    return ans.strip("0")

start = time.time()
print("part1",parseFile(file,1))
middle = time.time()
#print("part2",parseFile(file,2))
#end = time.time()

print(f"Part 1 runs in {middle - start}s")
#print(f"Part 2 runs in {end - middle}s")
