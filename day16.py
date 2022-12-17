from collections import defaultdict
#f = open("day16test.txt", "r")
f = open("day16input.txt", "r")
s = f.read().splitlines()
Gate = defaultdict(bool)
Rate = defaultdict(int)
Tunnels = defaultdict(list)
for str in s:
    A = str.split(' ')
    Gate[A[1]] = False
    Rate[A[1]] = int(A[4].replace(';', '').replace('rate=', ''))
    Tunnels[A[1]] = [v.replace(',', '') for v in A[9:]]

# print(Gate)
# print(Rate)
# print(Tunnels)
REMAINING_TIME = 30
def part1() -> int:
    q = [('AA', REMAINING_TIME, ("",), 0, 0)]
    best = 0
    been = {}
    maxflow = sum(Rate.values())
    while q:
        current = q.pop()
        loc, Remaining_min, opened_old, score, flow = current
        if been.get((loc, Remaining_min), -1) >= score:
            continue
        opened = {x for x in opened_old}
        been[(loc, Remaining_min)] = score

        if Remaining_min <= 0:
            best = max(best, score)
            continue

        if flow == maxflow:
            q.append((loc, 0, tuple(opened), score + flow * Remaining_min, flow))
            continue

        nextScore = score + flow
        if Rate[loc] > 0 and loc not in opened:
            opened.add(loc)
            q.append((loc, Remaining_min-1, tuple(opened),
                     nextScore, flow + Rate[loc]))
            opened.discard(loc)

        for neigh in Tunnels[loc]:
            q.append((neigh, Remaining_min-1, tuple(opened), nextScore, flow))

    return best
# print('part1:',part1())

def part2() -> int:
    q = [('AA', 'AA', REMAINING_TIME-4, ("",), 0, 0)]
    best = 0
    been = {}
    maxflow = sum(Rate.values())
    while q:
        current = q.pop()
        loc1, loc2, Remaining_min, opened_old, score, flow = current
        opened = {x for x in opened_old}

        opened_str = "".join(sorted(opened))
        #if been.get((loc1, loc2, Remaining_min,opened_str), -1) >= score:
        prev = been.get((loc1, loc2, Remaining_min), [-1,-1])
        if prev[0] >= score and prev[1] >= flow:
            continue
        been[(loc1, loc2, Remaining_min)] = [score,flow]

        if Remaining_min <= 0:
            best = max(best, score)
            continue

        if flow >= maxflow:
            q.append((loc1, loc2, 0, tuple(opened),
                     score + flow * Remaining_min, flow))
            continue

        nextScore = score + flow
        # open 1
        if loc1 not in opened and Rate[loc1] > 0:
            opened.add(loc1)
            # have to be diff location, open 2 too
            if loc1 != loc2 and loc2 not in opened and Rate[loc2] > 0:
                opened.add(loc2)
                q.append((loc1, loc2, Remaining_min-1, tuple(opened),
                         nextScore, flow+Rate[loc1]+Rate[loc2]))
                opened.discard(loc2)
            else:
                # cannot open 2
                for neigh2 in Tunnels[loc2]:
                    q.append((loc1, neigh2, Remaining_min-1,
                             tuple(opened), nextScore, flow+Rate[loc1]))
            opened.discard(loc1)
        # cannot open 1, but can open 2
        elif loc2 not in opened and Rate[loc2] > 0:
            opened.add(loc2)
            for neigh1 in Tunnels[loc1]:
                q.append((neigh1, loc2, Remaining_min-1,
                         tuple(opened), nextScore, flow+Rate[loc2]))
            opened.discard(loc2)
        # not open for both, both move on
        for neigh1 in Tunnels[loc1]:
            for neigh2 in Tunnels[loc2]:
                q.append((neigh1, neigh2, Remaining_min-1,
                         tuple(opened), nextScore, flow))
    return best


print('part2:', part2())
