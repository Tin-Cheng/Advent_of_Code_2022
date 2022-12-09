f = open("input.txt", "r")
A, X = ord("A"), ord("X")
score = [[1,0,2],[2,1,0],[0,2,1]]
win = [0,3,6]
tot, tot2 = 0, 0

for s in f:
    s = s.replace("\n","")
    a,b = s.split(" ")
    oa,ob = ord(a) - A, ord(b)-X
    
    #part 1
    tot += win[score[ob][oa]]
    tot += ob + 1

    #part 2
    tot2 += win[ob]
    tot2 += (oa + ob - 1) % 3
    tot2 += 1
print(tot)
print(tot2)