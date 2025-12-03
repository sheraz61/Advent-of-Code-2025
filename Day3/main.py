# Part 2
def max_two_digit(line):
    mx = -1
    for i in range(len(line) - 1):
        for j in range(i+1,len(line)):
            val = int(line[i]) * 10 +int(line[j])
            mx=max(mx,val)
    return mx

total = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        total += max_two_digit(line)

print(total)

# part 2
def max_12_digit_joltage(bank):
    n = len(bank)
    k = 12
    stack = []
    remove_count = n - k  # digits we can remove

    for digit in bank:
        while stack and remove_count > 0 and stack[-1] < digit:
            stack.pop()
            remove_count -= 1
        stack.append(digit)
    
    # take the first 12 digits
    return int(''.join(stack[:12]))

# total sum
total = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        total += max_12_digit_joltage(line)

print(total)
