n = int(input())

points = {}
for _ in range(n):
    point = tuple(map(int, input().split()))
    if point[0] in points:
        if points[point[0]][1] > point[1]:
            points[point[0]] = point    
    else:
        points[point[0]] = point

answer = 0
for value in points.values():
    answer += value[1]

print(answer)