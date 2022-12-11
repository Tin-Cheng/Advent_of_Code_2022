from copy import deepcopy
#f = open("day11test.txt", "r")
f = open("day11input.txt", "r")
s = f.read().splitlines()
Monkeys = []
for i in range(0,len(s),7):
    items = s[i+1].split(':')[-1].split(',')
    opt = s[i+2].split('=')[-1]
    test = int(s[i+3].split(' ')[-1])
    t = int(s[i+4].split(' ')[-1])
    f = int(s[i+5].split(' ')[-1])
    #item,operation,test,true,false
    monkey = [items,opt,test,t,f]
    #print(monkey)
    Monkeys.append(monkey)

def Worry(M,part):
    Monkeys = deepcopy(M)
    common = 1
    for monkey in Monkeys:
        common *= monkey[2]
    Inspect = [0] * len(Monkeys)
    times = 20 if part == 1 else 10000
    for _ in range(times):
        for i,monkey in enumerate(Monkeys):
            while monkey[0]:
                Inspect[i] += 1
                item = monkey[0].pop(0)
                new = eval(monkey[1].replace('old',str(item)))
                if part == 1: new = new // 3
                if part == 2: new = new % common
                if new % monkey[2] == 0:
                    Monkeys[monkey[3]][0].append(new)
                else:
                    Monkeys[monkey[4]][0].append(new)
    Inspect.sort(reverse=True)
    print(Inspect[0] *Inspect[1])
Worry(Monkeys,1)
Worry(Monkeys,2)