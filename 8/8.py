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
    return

data = open("8/input.txt").read().split("\n")
print(solve(data))