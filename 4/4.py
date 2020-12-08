def solve(data):
    essential = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0
    for passport in data:
        keys = []
        values = []
        for line in passport.split("\n"):
            for kvPair in line.split():
                keys.append(kvPair.split(":")[0])
                values.append(kvPair.split(":")[1])
        condition = True
        for e in essential:
            if e not in keys:
                condition = False
        if condition:
            valid += 1

    return valid

def solve2(data):
    essential = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0
    for passport in data:
        keys = []
        values = []
        for line in passport.split("\n"):
            for kvPair in line.split():
                keys.append(kvPair.split(":")[0])
                values.append(kvPair.split(":")[1])
        
        condition = True
        for k in keys:
            v = values[keys.index(k)]
            if k == "byr":
                if not 1920 <= int(v) <= 2002:
                    condition = False
            elif k == "iyr":
                if not 2010 <= int(v) <= 2020:
                    condition = False
            elif k == "eyr":
                if not 2020 <= int(v) <= 2030:
                    condition = False
            elif k == "hgt":
                pre = v[len(v) - 2:]
                post = v[:len(v) - 2]
                if pre == "in":
                    if not 59 <= int(post) <= 76:
                        condition = False
                elif pre == "cm":
                    if not 150 <= int(post) <= 193:
                        condition = False
                else:
                    condition = False
            elif k == "hcl":
                if len(v) == 7:
                    if v[0] == "#":
                        for char in v[1:]:
                            if not char in "a b c d e f 0 1 2 3 4 5 6 7 8 9".split():
                                condition = False
                    else:
                        condition = False
                else:
                    condition = False
            elif k == "ecl":
                if not v in ["amb","blu","brn","gry","grn","hzl","oth"]:
                    condition = False
            elif k == "pid":
                if len(v) != 9 or not v.isnumeric():
                    condition = False

        for e in essential:
            if e not in keys:
                condition = False
        if condition:
            valid += 1

    return valid


data = open("4/input.txt").read().split("\n\n")
print(solve2(data))
