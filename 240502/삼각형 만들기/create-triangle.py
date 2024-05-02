N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i==j or j==k or i==k:
                continue

            width = None
            height = None
            if points[i][0] == points[j][0] and points[i][1] == points[k][1]:
                height = abs(points[i][1]-points[j][1])
                width = abs(points[i][0]-points[k][0])

            
            if width and height:
                answer = max(answer, width*height)

print(answer)