n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

answer = float('inf')

for i in range(n):
    for j in range(i+1, n):
        distance = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
        answer = min(distance, answer)

print(answer)