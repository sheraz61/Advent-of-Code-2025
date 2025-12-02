
# Part 1
def isInvalid(num):
    s=str(num)
    n=len(s)
    return n%2==0 and s[:n//2] == s[n//2:]
total_sum=0


with open("input.txt") as f:
    text=f.read().strip()

ranges=text.split(",")
for r in ranges:
        r=r.strip()
        if not r:
            continue
        
        start, end=map(int,r.split("-"))
        if start>end:
            start,end=end,start
        for x in range(start,end+1):
            if isInvalid(x):
                total_sum+=x
    
if total_sum>0:
    print(total_sum)

# Part 2
def isInvalid(num):
    s=str(num)
    n=len(s)
    for k in range(1,n//2+1):
         if n%k==0:
              if s[:k]*(n//k)==s:
                   return True
    return False
total_sum=0


with open("input.txt") as f:
    text=f.read().strip()

ranges=text.split(",")
for r in ranges:
        r=r.strip()
        if not r:
            continue
        
        start, end=map(int,r.split("-"))
        if start>end:
            start,end=end,start
        for x in range(start,end+1):
            if isInvalid(x):
                total_sum+=x
    
if total_sum>0:
    print(total_sum)

