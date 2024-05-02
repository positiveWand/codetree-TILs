N = int(input())

lines = [tuple(map(int, input().split())) for _ in range(N)]

overlap = set()

for i in range(N):
    for j in range(i+1, N):
        if (lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1])\
        or (lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1]):
            overlap.add(lines[i])
            overlap.add(lines[j])

answer = 0
for l in lines:
    if l not in overlap:
        answer += 1

print(answer)