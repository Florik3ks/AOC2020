def solve(data):
    c = 0
    num = []
    for line in data:
        c += 1
        if c > 25:
            check = False
            for n in num:
                for n2 in num:
                    if n != n2 and n + n2 == int(line):
                        check = True
            if not check:
                return line
            num.pop(0)
        num.append(int(line))
    return None

def solve2(data):
    c = 0
    num = []
    allnum = []
    for line in data:
        c += 1
        if c > 25:
            check = False
            for n in num:
                for n2 in num:
                    if n != n2 and n + n2 == int(line):
                        check = True
            if not check:
                for start in range(len(allnum)):
                    for end in range(len(allnum[start:]) - 1):
                        sumOfRange = 0
                        for i in allnum[start:end + start + 2]:
                            sumOfRange += i
                        if sumOfRange == int(line):
                            minimum = allnum[start]
                            maximum = allnum[start]
                            for n in allnum[start:end + start + 2]:
                                minimum = min(minimum, n)
                                maximum = max(maximum, n)
                            return minimum + maximum

            num.pop(0)
        num.append(int(line))
        allnum.append(int(line))
    return None

data = open("09/input.txt").read().split("\n")
print(solve2(data))
