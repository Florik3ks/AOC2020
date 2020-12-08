def solve(data):
    valid = 0
    for line in data:
        character = line[line.index(":") - 1]
        minimum = int(line.split("-")[0])
        maximum = ""
        for c in line.split("-")[1]:
            maximum += c
            if c == " ":
                break
        maximum = int(maximum)
        count = 0
        for char in line.split(":")[1]:
            if char == character:
                count += 1
        if minimum <= count <= maximum:
            valid += 1
    return valid


def solve2(data):
    valid = 0
    for line in data:
        character = line[line.index(":") - 1]
        index1 = int(line.split("-")[0]) - 1
        index2 = ""
        for c in line.split("-")[1]:
            index2 += c
            if c == " ":
                break
        index2 = int(index2) - 1
        password = line.split(":")[1].strip()
        if password[index1] == character and password[index2] != character or password[index1] != character and password[index2] == character:
            valid += 1
    return valid


data = open("2/input.txt").read().split("\n")

print(solve2(data))
