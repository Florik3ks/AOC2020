
def solve(data):
    arrival = int(data[0])
    busIDs = [int(x) for x in data[1].split(",") if x != "x"]
    earliestBus = busIDs[0]
    waitingTime = earliestBus - (arrival % earliestBus)
    for bID in busIDs:
        if bID - (arrival % bID) < waitingTime:
            earliestBus = bID
            waitingTime = earliestBus - (arrival % earliestBus)

    return earliestBus * waitingTime


def solve2(data):  # way too slow
    busIDs = {}
    splittedList = data[1].split(",")
    
    for i in range(len(splittedList)):
        if splittedList[i] != "x":
            busIDs[splittedList[i]] = str(i)

    sortedList = [int(x) for x in splittedList if x != "x"]
    sortedList.sort(reverse=True)
    steps = sortedList[0]
    
    t = -int(busIDs[str(steps)])

    breakCon = False
    while not breakCon:
        breakCon = True
        for k in busIDs.keys():
            if (t + int(busIDs[k])) % int(k) != 0:
                breakCon = False
                break
        if breakCon:
            return t

        t += steps

    return None


# def solve2_2(data):
#     # idk how to implement but
#     # https://brilliant.org/wiki/chinese-remainder-theorem/

#     buses = [(int(i), int(e)) for i, e in enumerate(data[1].split(",")) if e != "x"]

#     bIDs = [t for _, t in buses]
#     offsets = [time-i for i, time in buses]

#     from math import log, exp
#     N = exp(sum(map(log, bIDs)))

#     return


    


data = open("13/input.txt").read().split("\n")
print(solve2(data))

