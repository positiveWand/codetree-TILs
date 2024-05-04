N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

finished = False
for i in range(11):
    for j in range(11):
        for k in range(11):
            valid = [False for _ in range(N)]
            for idx, p in enumerate(points):
                if i == p[0] or j == p[1] or k == p[0]:
                    valid[idx] = True
            if not finished and all(valid):
                print(1)
                finished = True
                
        for k in range(11):
            valid = [False for _ in range(N)]
            for idx, p in enumerate(points):
                if i == p[0] or j == p[1] or k == p[1]:
                    valid[idx] = True
            if not finished and all(valid):
                print(1)
                finished = True

if not finished:
    print(0)