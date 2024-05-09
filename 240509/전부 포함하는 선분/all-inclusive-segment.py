n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

answer = float('inf')
for excluded in range(n):
    start = float('inf')
    end = 0
    for i, line in enumerate(lines):
        if i == excluded:
            continue
        
        start = min(start, line[0], line[1])
        end = max(end, line[0], line[1])

    answer = min(end-start, answer)

print(answer)