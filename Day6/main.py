numbers = []
operators = []

with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

# Last line contains operators
operators = lines[-1].split()

# All previous lines contain numbers
for row in lines[:-1]:
    numbers.append(list(map(int, row.split())))

# ---- Calculate total ----
total = 0
cols = len(operators)

for c in range(cols):

    if operators[c] == '+':
        col_sum = sum(row[c] for row in numbers)
        total += col_sum

    elif operators[c] == '*':
        product = 1
        for row in numbers:
            product *= row[c]
        total += product

print("Total =", total)



def solve(filename):
    lines = [l.rstrip("\n") for l in open(filename) if l.strip()]

    ops = lines[-1]
    rows = lines[:-1]

    w = max(len(r) for r in lines)
    rows = [r.ljust(w) for r in rows]
    ops = ops.ljust(w)

    cols = []
    for c in range(w):
        nums = "".join(rows[r][c] for r in range(len(rows))).replace(" ", "")
        cols.append(nums)   # "" means separator column

    total = 0
    i = w - 1  # right → left

    while i >= 0:
        if cols[i] == "":
            i -= 1
            continue

        nums = []
        op = None

        while i >= 0 and cols[i] != "":
            nums.append(int(cols[i]))
            if ops[i] != " ":
                op = ops[i]
            i -= 1

        if op == "+":
            total += sum(nums)
        else:  # "*"
            p = 1
            for n in nums:
                p *= n
            total += p

    return total


print(solve("input.txt"))
