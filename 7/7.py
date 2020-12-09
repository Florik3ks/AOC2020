def solve(data):
    c = 0
    q = ["shiny gold"]
    done = []
    while len(q) > 0:
        for line in data:
            if "no other bags" in line:
                continue
            line = line.replace(".", "").replace("bags", "").replace("bag", "")
            bag = line.split("contain")[0].strip()
            bags = line.split("contain")[1].strip().split(",")
            contains = []
            for b in bags:
                contains.append(' '.join(b.split()[1:]).strip())
            if q[0] in contains:
                if bag not in done and bag not in q:
                    q.append(bag)

        done.append(q.pop(0))
    c = len(done) - 1
    return c


def solve2(data):
    c = 0
    bags = {}
    
    for line in data:
        line = line.replace(".", "").replace("bags", "").replace("bag", "")
        bag = line.split("contain")[0].strip()

        contains_str = line.split("contain")[1].strip().split(",")
        contains = []
        if not "no other" in contains_str:
            for b in contains_str:
                contains.append(' '.join(b.split()).strip())
        bags[bag] = contains
    
    q = [bags["shiny gold"]]
    c = 0
    while len(q) > 0:
        for b in q.pop(0):
            bag = ' '.join(b.split()[1:])
            count = int(b.split()[0])
            for i in range(count):
                q.append(bags[bag])
            c += count
    return c

data = open("7/input.txt").read().split("\n")
print(solve2(data))
