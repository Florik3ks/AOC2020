def solve(data):
    memory = {}
    mask = ""
    for cmd in data:
        if "mask" in cmd:
            mask = cmd.split("= ")[1]
            continue
        address = cmd[cmd.find("[")+ 1 : cmd.rfind("]")]
        value = str(bin(int(cmd.split("= ")[1])))[2:]
        value = ((len(mask) - len(value)) * "0") + value
        result = list(value)
        for i in range(len(mask)):
            if mask[i] != "X":
                result[i] = mask[i]
        memory[address] = int(''.join(result), 2)
    
    result = 0
    for k in memory.keys():
        result += memory[k]
    return result


def solve2(data):
    memory = {}
    mask = ""
    for cmd in data:
        if "mask" in cmd:
            mask = cmd.split("= ")[1]
            continue
        address = cmd[cmd.find("[")+ 1 : cmd.rfind("]")]
        value = str(bin(int(cmd.split("= ")[1])))[2:]
        value = ((len(mask) - len(value)) * "0") + value
        result = list(value)
        for i in range(len(mask)):
            if mask[i] != "X":
                result[i] = mask[i]
        memory[address] = int(''.join(result), 2)
    
    result = 0
    for k in memory.keys():
        result += memory[k]
    return result

data = open("14/input.txt").read().split("\n")
print(solve(data))