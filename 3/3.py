def solve(data):
    c = 0
    xPos = 0
    for yPos in range(len(data)):
        if data[yPos][xPos] == "#":
            c += 1
        xPos += 3
        xPos = xPos % len(data[0])
    return c

def solve2(data):
    xSteps = [1,3,5,7,1]
    ySteps = [1,1,1,1,2]
    result = 1
    for i in range(len(xSteps)):
        c = 0
        xPos = 0
        for yPos in range(0, len(data), ySteps[i]):
            if data[yPos][xPos] == "#":
                c += 1
            xPos += xSteps[i]
            xPos = xPos % len(data[0])
        result = result * c
    return result

data = open("3/input.txt").read().split("\n")
print(solve2(data))