def solve(data):
    def move(action, number):
        x = 0
        y = 0
        if action == "N":
            y += number
        elif action == "E":
            x += number
        elif action == "S":
            y -= number
        elif action == "W":
            x -= number
        return x, y

    dirs = ["N", "E", "S", "W"]
    x = 0
    y = 0
    direction = "E"
    for instruction in data:
        action = instruction[0]
        number = int(instruction[1:])

        if action == "F":
            action = direction
        elif action == "L":
            i = dirs.index(direction)
            direction = dirs[(i - (number // 90)) % 4]
        elif action == "R":
            i = dirs.index(direction)
            direction = dirs[(i + (number // 90)) % 4]

        xy = move(action, number)
        x += xy[0]
        y += xy[1]

    return abs(x) + abs(y)


def solve2(data):
    ship = {
        "N": 0,
        "E": 0,
        "S": 0,
        "W": 0
    }
    waypoint = {
        "N": 1,
        "E": 10,
        "S": 0,
        "W": 0
    }
    for instruction in data:
        action = instruction[0]
        number = int(instruction[1:])

        if action == "F":
            for k in ship.keys():
                ship[k] += waypoint[k] * number
        elif action == "L":
            for i in range(number // 90):
                waypoint['N'], waypoint['E'], waypoint['S'], waypoint['W'] = waypoint['E'], waypoint['S'], waypoint['W'], waypoint['N']

        elif action == "R":
            for i in range(number // 90):
                waypoint['E'], waypoint['S'], waypoint['W'], waypoint['N'] = waypoint['N'], waypoint['E'], waypoint['S'], waypoint['W']

        else:
            waypoint[action] += number

    return abs(ship["E"] - ship["W"]) + abs(ship["N"] - ship["S"])


data = open("12/input.txt").read().split("\n")
print(solve2(data))
