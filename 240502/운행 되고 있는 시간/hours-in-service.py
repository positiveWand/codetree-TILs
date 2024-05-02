N = int(input())

devs = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(N):
    online = []
    for j in range(N):
        if i==j:
            continue
        
        online.append(None)
        while online:
            time = online.pop(0)
            if not time:
                online.append(devs[j])
                break
            
            time_start, time_end = time
            if time_start <= devs[j][0] < time_end:
                online.append((min(time_start, devs[j][0]), devs[j][1]))
                online.remove(None)
                break
            elif time_start <= devs[j][1] < time_end:
                online.append((devs[j][0], min(time_end, devs[j][1])))
                online.remove(None)
                break
            else:
                online.append((time_start, time_end))
        
    total = 0
    for start, end in online:
        total += end-start
    
    # print(online)
    
    answer = max(answer, total)

print(answer)