N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

answer = float('inf')
for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        area = [0,0,0,0]
        for x,y in points:
            if x < i and y < j:
                area[0] += 1
            elif x < i and y > j:
                area[1] += 1
            elif x > i and y < j:
                area[2] += 1
            elif x > i and y > j:
                area[3] += 1

        answer = min(answer, max(area))

print(answer)