n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

possible = False
for i in range(n):
    max_start = max(lines[:i]+lines[i+1:], key=lambda x: x[0])[0]
    min_end = min(lines[:i]+lines[i+1:], key=lambda x: x[1])[1]

    if max_start <= min_end:
        possible = True
        break

if possible:
    print('Yes')
else:
    print('No')