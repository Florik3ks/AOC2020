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
    
    def getAllAdresses(_result, index):
        result = list(_result)
        if index >= len(result):
            floatingAddresses.append(result)
            return
        if result[index] == "X":
            for i in range(2):
                result[index] = str(i)
                getAllAdresses(result, index + 1)
                result[index] = "X"
        else:
            getAllAdresses(result, index + 1)



    floatingAddresses = []
    memory = {}
    mask = ""
    for cmd in data:
        if "mask" in cmd:
            mask = cmd.split("= ")[1]
            continue
        address = cmd[cmd.find("[")+ 1 : cmd.rfind("]")]

        value = cmd.split("= ")[1]
        binAddress = str(bin(int(address)))[2:]
        binAddress = ((len(mask) - len(binAddress)) * "0") + binAddress

        result = list(binAddress)
        for i in range(len(mask)):
            if mask[i] == "0":
                result[i] = result[i]
            elif mask[i] == "1":
                result[i] = "1"
            elif mask[i] == "X":
                result[i] = "X"
        floatingAddresses = []
        getAllAdresses(result, 0)
        for r in floatingAddresses:
            memory[int(''.join(r), 2)] = value
    
    result = 0
    for k in memory.keys():
        result += int(memory[k])
    return result

data = open("14/input.txt").read().split("\n")
print(solve2(data))