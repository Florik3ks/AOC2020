def solve(data):
    c = 0
    for group in data:
        questions = []
        for person in group.split("\n"):
            for question in person:
                if question not in questions:
                    questions.append(question)
        c += len(questions) 
    return c

def solve2(data):
    c = 0
    for group in data:
        questions = []
        if len(group.split("\n")) > 0:
            questions = list(group.split("\n")[0])
        for person in group.split("\n"):
            q2 = list(questions) # copy
            for i in range(len(questions)):
                if not questions[i] in list(person):
                    q2.remove(questions[i])
            questions = q2
        c += len(questions)
    return c

data = open("06/input.txt").read().split("\n\n")
print(solve2(data))