import math
#f = open("day21test.txt", "r")
f = open("day21input.txt", "r")
#f = open("day21test2.txt", "r")
file = f.read().splitlines()
Monkeys = {}
for i,line in enumerate(file):
    A = line.split(":")
    Monkeys[A[0]] = A[1].lstrip()
#print(Monkeys)

def part1(Monkeys):
    def evalMonkey(name):
        monkey = Monkeys[name]
        A = Monkeys[name].split(" ")
        if len(A) == 1: return int(A[0])
        else:
            A[0] = evalMonkey(A[0])
            A[2] = evalMonkey(A[2])
            if A[1] == "+": return A[0] + A[2]
            elif A[1] == "-": return A[0] - A[2]
            elif A[1] == "*": return A[0] * A[2]
            elif A[1] == "/": return A[0] // A[2]
            print("error",name,monkey)
            return 0
    return evalMonkey("root")
print("part1:", part1(Monkeys))
#3916491093817
def part2(Monkeys):
    low, hi = 0,9999999999999999999999
    mid = (low + hi) // 2
    def evalMonkey(name):
        if name == 'humn': return mid
        A = Monkeys[name].split(" ")
        if len(A) == 1: return int(A[0])
        else:
            A[0] = evalMonkey(A[0])
            A[2] = evalMonkey(A[2])
            if name == "root": return A[0] - A[2]
            elif A[1] == "+": return A[0] + A[2]
            elif A[1] == "-": return A[0] - A[2]
            elif A[1] == "*": return A[0] * A[2]
            elif A[1] == "/": return A[0] // A[2]
            return 0
    while low < hi:
        mid = (low + hi) // 2
        tmp = evalMonkey("root")
        #print(low,hi,mid,tmp)
        if tmp == 0: return mid
        elif tmp > 0: 
            low = mid + 1
        else:
            hi = mid - 1
    return mid
# def part2(Monkeys):
#     HaveHuman = {}
#     def LookForHumn(name):
#         if name == 'humn': HaveHuman[name] = True
#         else: 
#             monkey = Monkeys[name]
#             if monkey.isnumeric(): HaveHuman[name] = False
#             else:
#                 A = monkey.split(" ")
#                 l,r = LookForHumn(A[0]), LookForHumn(A[2])
#                 HaveHuman[name] = l or r
#         return HaveHuman[name] 
        
#     def evalMonkey(name):
#         monkey = Monkeys[name]
#         if monkey.isnumeric(): return int(monkey)
#         else:
#             A = monkey.split(" ")
#             A[0] = evalMonkey(A[0])
#             A[2] = evalMonkey(A[2])
#             if A[1] == "+": return A[0] + A[2]
#             elif A[1] == "-": return A[0] - A[2]
#             elif A[1] == "*": return A[0] * A[2]
#             elif A[1] == "/": return A[0] / A[2]
#             return 0
#     def match(name,target):
#         if name == 'humn': return target
#         monkey = Monkeys[name].split(" ")
#         left = evalMonkey(monkey[0])
#         right = evalMonkey(monkey[2])
#         print(name,target,monkey,HaveHuman[monkey[0]], (right if HaveHuman[monkey[0]] else left))
#         if HaveHuman[monkey[0]]:
#             if monkey[1] == "+": target -= right
#             elif monkey[1] == "-": target += right
#             elif monkey[1] == "*": target = div_exact(target, right)
#             elif monkey[1] == "/": target *= right
#             #return match(monkey[0],math.ceil(target))
#             return match(monkey[0],target)
#         else:
#             if monkey[1] == "+": target -= left
#             elif monkey[1] == "-": target += left
#             elif monkey[1] == "*": target = div_exact(target, left)
#             elif monkey[1] == "/": target *= left
#             #return match(monkey[2],math.ceil(target))
#             return match(monkey[2],target)

#     root = Monkeys['root'].split(" ")
#     _,_ = LookForHumn(root[0]),LookForHumn(root[2])
#     print(root,evalMonkey(root[0]),evalMonkey(root[2]))
#     if HaveHuman[root[0]]:
#         return match(root[0],evalMonkey(root[2]))
#     else:
#         return match(root[2],evalMonkey(root[0]))

#print(Monkeys)
print("part2:", part2(Monkeys))