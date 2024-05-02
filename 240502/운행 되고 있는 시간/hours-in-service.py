N = int(input())

devs = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(N):
    online = [0 for _ in range(1001)]
    for j in range(N):
        if i==j:
            continue
        
        for time in range(devs[j][0],devs[j][1]):
            online[time] += 1
        
    total = 0
    for t in online:
        if t > 0:
            total += 1
    
    answer = max(answer, total)

print(answer)