N = int(input())

points = [tuple(map(int, input().split())) for _ in range(N)]
# print(points)

answer = float('inf')

for i in range(N):
    eliminated = points[i]

    min_x = float('inf')
    max_x = 0
    min_y = float('inf')
    max_y = 0

    for j in range(N):
        if i == j:
            continue
        
        min_x = min(min_x, points[j][0])
        max_x = max(max_x, points[j][0])
        min_y = min(min_y, points[j][1])
        max_y = max(max_y, points[j][1])

    answer = min(answer, abs(max_x - min_x) * abs(max_y - min_y))

print(answer)