def solve(data, num):
    from collections import defaultdict
    data = [int(i) for i in data[0].split(",")]
    numbers = defaultdict(int)
    nextNum = data[0]
    previousNumTurn = 0
    for turn in range(1, int(num)):
        # print(str(turn) + ": " + str(nextNum))
        previousNumTurn = numbers[nextNum]
        numbers[nextNum] = turn
        if turn < len(data):
            nextNum = data[turn]
        elif turn == len(data):
            nextNum = 0
        elif previousNumTurn == 0:
            nextNum = 0
        else:
            diff = numbers[nextNum] - previousNumTurn
            numbers[nextNum] = turn
            nextNum = diff

    return nextNum


data = open("15/input.txt").read().split("\n")
print(solve(data, data[1]))
print(solve(data, data[2])) # kinda slow