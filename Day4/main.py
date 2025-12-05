#part 1
grid = []

with open("input.txt") as f:
    for line in f:
        grid.append(line.strip())

rows = len(grid)
cols = len(grid[0])

# Directions for 8 neighbors
directions = [
    (-1,-1), (-1,0), (-1,1),
    ( 0,-1),         ( 0,1),
    ( 1,-1), ( 1,0), ( 1,1)
]

count_accessible = 0

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != '@':
            continue
        
        neighbors = 0
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    neighbors += 1

        # Rule:
        if neighbors < 4:
            count_accessible += 1

print(count_accessible)

# part 2
grid = []

with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])

directions = [
    (-1,-1), (-1,0), (-1,1),
    ( 0,-1),         ( 0,1),
    ( 1,-1), ( 1,0), ( 1,1)
]

total_removed = 0

while True:
    to_remove = []

    # STEP 1: find all accessible rolls
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbors += 1

            if neighbors < 4:
                to_remove.append((r, c))

    # STOP CONDITION
    if not to_remove:
        break

    # STEP 2: remove them all at once
    for r, c in to_remove:
        grid[r][c] = '.'

    total_removed += len(to_remove)

print(total_removed)
