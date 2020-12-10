def solve(data):
    diff1 = 0
    diff3 = 0
    for i in range(len(data)):
        data[i] = int(data[i])
    data.sort()
    data.append(data[len(data) - 1] + 3)
    last = 0
    for i in data:
        if last + 1 == i:
            diff1 += 1
        elif last + 2 == i:
            pass
        elif last + 3 == i:
            diff3 += 1
        last = i
    
    return diff1, diff3, diff1 * diff3

def solve2(data):
    for i in range(len(data)):
        data[i] = int(data[i])
    data.sort()
    data.append(data[len(data) - 1] + 3)
    data.append(0)
    data.sort()

    from collections import defaultdict
    ways = defaultdict(int)
    ways[0] = 1

    for i in range(1, len(data)):
        ways[data[i]] = ways[data[i]-1] + ways[data[i]-2] + ways[data[i]-3]

    return ways[data[-1]]


data = open("10/input.txt").read().split("\n")
print(solve2(data))