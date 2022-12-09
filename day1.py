f = open("day1input.txt", "r")
elves = []
maxamt = 0
cur = 0
for s in f:
    s = s.replace("\n","")
    if s.isnumeric():
        #print("in",s)
        cur += int(s)
    else:
        maxamt = max(maxamt,cur)
        elves.append(cur)
        cur = 0
    #print(s)
maxamt = max(maxamt,cur)
elves.append(cur)
elves.sort(reverse=True)
print("top 1 amt: ", maxamt)
print("sum of top 3: ",sum(elves[:3]))