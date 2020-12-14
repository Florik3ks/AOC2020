def solve(data):
    visitedLines = []
    instruction = data[0]
    instructionLine = 0
    acc = 0
    while instructionLine not in visitedLines:
        instruction = data[instructionLine]
        visitedLines.append(instructionLine)

        instr = instruction.split()[0]
        num = instruction.split()[1]
        if instr == "acc":
            acc += int(num)
        elif instr == "jmp":
            instructionLine = instructionLine + int(num) - 1
        instructionLine += 1

    return acc

def solve2(data):
    
    for line in range(len(data)):
        oldline = data[line]
        if oldline.split()[0] == "jmp":
            data[line] = "nop " + oldline.split()[1]
        elif oldline.split()[0] == "nop":
            data[line] = "jmp " + oldline.split()[1]
        

        visitedLines = []
        instruction = data[0]
        instructionLine = 0
        acc = 0

        while instructionLine not in visitedLines:
            instruction = data[instructionLine]
            visitedLines.append(instructionLine)

            instr = instruction.split()[0]
            num = instruction.split()[1]
            if instr == "acc":
                acc += int(num)
            elif instr == "jmp":
                instructionLine = instructionLine + int(num) - 1
            instructionLine += 1

            if instructionLine >= len(data):
                return acc
            
        data[line] = oldline

    return None

data = open("08/input.txt").read().split("\n")
print(solve2(data))