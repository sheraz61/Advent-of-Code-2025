# ranges =[]
# ids=[]
# with open ('input.txt','r') as f:
#     for line in f:
#         line=line.strip()
#         if not line:
#             continue
#         if '-' in line :
#             start,end=map(int,line.split('-'))
#             ranges.append((start,end))
#         else:
#             ids.append(int(line))
# # print(ranges)
# # print(ids)
# count=0
# for id in ids:
#     for start,end in ranges:
#         if start<=id<=end:
#             count+=1
#             break

# print(count)

ranges =[]
ids=[]
with open ('input.txt','r') as f:
    for line in f:
        line=line.strip()
        if not line:
            continue
        if '-' in line :
            start,end=map(int,line.split('-'))
            ranges.append((start,end))
        else:
            ids.append(int(line))

ranges.sort()

total = 0
cur_start, cur_end = ranges[0]

for start, end in ranges[1:]:
    if start <= cur_end + 1:
        cur_end = max(cur_end, end)
    else:
        total += (cur_end - cur_start + 1)
        cur_start, cur_end = start, end

total += (cur_end - cur_start + 1)

print(total)

ranges =[] 
ids=[]

with open ('input.txt','r') as f:
    for line in f: 
        line=line.strip()
        if not line: 
            continue 
        if '-' in line :
            start,end=map(int,line.split('-'))
            ranges.append((start,end)) 
        else:
            ids.append(int(line))

count=0 

# ranges.sort() 

for start,end in ranges:
    curr=start 
    while curr >=start and curr<=end: 
        count+=1 
        curr+=1 

print(count)