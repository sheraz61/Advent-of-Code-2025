# Part 1
pos = 50
count = 0

with open("input.txt") as f:
    for line in f:
        inst = line.strip()
        direction = inst[0]
        steps = int(inst[1:])

        if direction == "R":
            pos = (pos + steps) % 100
        else:
            pos = (pos - steps) % 100

        if pos == 0:
            count += 1

print(count)

## Part 2
pos = 50
count = 0

with open("input2.txt") as f:
    for line in f:
        inst = line.strip()
        direction = inst[0]
        steps = int(inst[1:])
        
        for _ in range(steps):
            if direction == "R":
                pos = (pos + 1) % 100
            else:
                pos = (pos - 1) % 100

            if pos == 0:
                count += 1

print(count)


