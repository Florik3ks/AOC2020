import math

def solve(data):
    row = 0
    column = 0
    seatID = 0
    maxID = 0
    for line in data:
        start = 0
        end = 127
        for i in range(7):
            if line[i] == "F":
                end = math.floor(end - (end - start) / 2)
            elif line[i] == "B":
                start = math.ceil(start + (end - start) / 2)
        row = start
        start = 0
        end = 7
        for i in range(len(line)):
            if line[i] == "L":
                end = math.floor(end - (end - start) / 2)
            elif line[i] == "R":
                start = math.ceil(start + (end - start) / 2)
        column = start
        seatID = row * 8 + column
        maxID = max(seatID, maxID)
    return maxID

def solve2(data):
    row = 0
    column = 0
    seatID = 0
    seatIDs = []
    for line in data:
        start = 0
        end = 127
        for i in range(7):
            if line[i] == "F":
                end = math.floor(end - (end - start) / 2)
            elif line[i] == "B":
                start = math.ceil(start + (end - start) / 2)
        row = start
        start = 0
        end = 7
        for i in range(len(line)):
            if line[i] == "L":
                end = math.floor(end - (end - start) / 2)
            elif line[i] == "R":
                start = math.ceil(start + (end - start) / 2)
        column = start
        seatID = row * 8 + column
        seatIDs.append(seatID)

    current = seatIDs[0]
    seatIDs.sort()
    for current in seatIDs:
        if current + 2 in seatIDs and not current + 1 in seatIDs:
            return current + 1
    return None

data = open("5/input.txt").read().split("\n")
print(solve2(data))