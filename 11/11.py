def solve(data):
    def cycle(old, dirs):
        new = [row[:] for row in old]  # copy
        for y in range(len(old)):
            for x in range(len(old[y])):
                neighbours = 0
                for d in dirs:
                    try:
                        if y + d[1] >= 0 and x + d[0] >= 0:
                            if old[y + d[1]][x + d[0]] == "#":
                                neighbours += 1
                    except IndexError:
                        pass
                if neighbours >= 4 and old[y][x] == "#":
                    new[y][x] = "L"
                if neighbours == 0 and old[y][x] == "L":
                    new[y][x] = "#"
        return new

    dirs = [( -1,  -1), (0, -1), (+1, -1),
            ( -1,   0),          (+1,  0),
            ( -1,  +1), (0, +1), (+1, +1)]
    last = []
    new = [row[:] for row in data]  # copy
    while last != new:
        last = [row[:] for row in new]  # copy
        new = cycle(new, dirs)

    c = 0
    for y in new:
        for x in y:
            if x == "#":
                c += 1

    return c


def solve2(data):
    def cycle(old, dirs):
        new = [row[:] for row in old]  # copy
        for y in range(len(old)):
            for x in range(len(old[y])):
                neighbours = 0
                for d in dirs:
                    newY = y
                    newX = x
                    current = "."
                    while current == ".":
                        newY += d[1]
                        newX += d[0]
                        try:
                            if newY >= 0 and newX >= 0:
                                current = old[newY][newX]
                                if current == "#":
                                    neighbours += 1
                            else:
                                current = "not ."
                        except IndexError:
                            current = "not ."
                if neighbours >= 5 and old[y][x] == "#":
                    new[y][x] = "L"
                if neighbours == 0 and old[y][x] == "L":
                    new[y][x] = "#"
        return new

    dirs = [( -1,  -1), (0, -1), (+1, -1),
            ( -1,   0),          (+1,  0),
            ( -1,  +1), (0, +1), (+1, +1)]
    last = []
    new = [row[:] for row in data]  # copy
    while last != new:
        last = [row[:] for row in new]  # copy
        new = cycle(new, dirs)

    c = 0
    for y in new:
        for x in y:
            if x == "#":
                c += 1

    return c


data = open("11/input.txt").read().split("\n")
for i in range(len(data)):
    data[i] = list(data[i])
print(solve2(data))