def solve(data):
    for num in data:
        for num2 in data:
            if num != num2:
                if int(num) + int(num2) == 2020:
                    return int(num) * int(num2)

def solve2(data):
    for num in data:
        for num2 in data:
            for num3 in data:
                if num != num2 and num != num3 and num2 != num3:
                    if int(num) + int(num2) + int(num3) == 2020:
                        return int(num) * int(num2) * int(num3)
                        
data = open("01/input.txt").read().split("\n")
print(solve2(data))
                    