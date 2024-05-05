n, m = list(map(int, input().split()))

pairs = [tuple(map(int, input().split())) for _ in range(m)]

answer = 0
for i in range(m):
    target = pairs[i]
    count = 1
    for j in range(m):
        if i == j:
            continue
        if (target[0], target[1]) == pairs[j] or (target[1], target[0]) == pairs[j]:
            count += 1
    
    answer = max(count ,answer)

print(answer)