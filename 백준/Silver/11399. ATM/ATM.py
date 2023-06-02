n = int(input())
p = list(map(int, input().split()))
p.sort()
time = 0
total = 0
for i in range(0,len(p)):
    time += p[i]
    total += time
print(total)