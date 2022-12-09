f = open("input.txt", "r")
#f = open("test.txt", "r")
cur = []
total1 = 0
total2 = 0
for i,s in enumerate(f):
    s = s.replace('\n','')
    S = s.split(',')
    a1,a2 = S[0].split('-')
    b1,b2 = S[1].split('-')
    a1,a2,b1,b2 = int(a1),int(a2),int(b1),int(b2)
    #print(a1,a2,b1,b2)
    if a1 > b1:
        a1,a2,b1,b2 = b1,b2,a1,a2
    if (a1 < b1 and a2 >= b2) or (a1 == b1): 
        total1 += 1
    if a1 <= b2 and a2 >=b1:
        total2 += 1

print(total1)
print(total2)