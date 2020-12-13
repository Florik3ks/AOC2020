import os
import errno

template = open("template.txt","r").read()
for i in range(15,25):
    
    filename = f"{i}\\input.txt"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                continue
    with open(filename, "w") as f:
        f.write("")

    script = open(f"{i}\\{i}.py","w")
    script.write(template.replace("day", str(i)))
    script.close()
