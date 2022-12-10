#f = open("day10test.txt", "r")
f = open("day10input.txt", "r")
count = 1
cycle = 0
total = 0
pixels = []
pixel = ''
def AddToTotal():
    global total
    if (cycle - 20) % 40 == 0:
        total += cycle * count
def Draw():
    global pixel
    pixel += '#' if count <= len(pixel) + 1 and count + 2 >= len(pixel) + 1 else '.'
    if (cycle) % 40 == 0:
        pixels.append(pixel)
        pixel = ''
    return

for s in f:
    s = s.replace("\n","")
    A = s.split(" ")
    times = 1 + int(A[0] == 'addx')
    for _ in range(times):
        cycle += 1
        AddToTotal()
        Draw()
    count += int(A[1]) if A[0] == 'addx' else 0
    # if A[0] == 'noop':
    #     cycle += 1
    #     AddToTotal()
    #     Draw()
    # elif A[0] == 'addx':
    #     for _ in range(2):
    #         cycle += 1
    #         AddToTotal()
    #         Draw()
    #     count += int(A[1])
    # else:
    #     print('error')
print(total)
for pixel in pixels:
    print(pixel)