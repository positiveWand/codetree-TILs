N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

finished = False
for a,b,c in [(0,0,0),(0,0,1),(0,1,1),(1,1,1)]:
    for i in range(11):
        for j in range(11):
            for k in range(11):
                valid = [False for _ in range(N)]
                for idx, p in enumerate(points):
                    if i == p[a] or j == p[b] or k == p[c]:
                        valid[idx] = True
                if not finished and all(valid):
                    print(1)
                    finished = True

if not finished:
    print(0)