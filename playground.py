x = eval("[1,2,3]")
print(x,type(x))

x = list(map(str.splitlines, open("day13test.txt").read().strip().split("\n\n")))
print(x,type(x))
for i, (a, b) in enumerate(x):
    print(a,type(a))
    print(b,type(b))
    xa = eval(a)
    xb = eval(b)
    print(xa,type(xa))
    print(xb,type(xb))
    for xai,xbi in zip(xa,xb):
        print(xai,type(xai))
        print(xbi,type(xbi))
