N = int(input())
seats = list(map(int, list(input())))

# 양 끝 점 구하기
start = 0
end = N-1
while seats[start]!=1:
    start+=1
while seats[end]!=1:
    end-=1

if start == end:
    print(max(start-0, N-1-start))
else:
    candidates = []

    # 가장 가까운 2개 위치 계산
    furthest = None
    max_distance = 0
    before = None
    for i in range(N):
        if seats[i] == 1:
            if  before != None and max_distance < i-before:
                max_distance = i-before
                furthest = (before, i)
            before = i

    seats[(furthest[1]+furthest[0])//2] = 1

    # 거리 최소값 계산
    min_distance = float('inf')
    before = None
    for i in range(N):
        if seats[i] == 1:
            if before != None:
                min_distance = min(min_distance, i-before)
            before = i

    candidates.append(min_distance)
    # print(seats)
    # print(candidates)

    seats[(furthest[1]+furthest[0])//2] = 0

    if seats[0] == 0:
        seats[0] = 1

        # 거리 최소값 계산
        min_distance = float('inf')
        before = None
        for i in range(N):
            if seats[i] == 1:
                if before != None:
                    min_distance = min(min_distance, i-before)
                before = i

        candidates.append(min_distance)
        seats[0] = 0
    if seats[N-1] == 0:
        seats[N-1] = 1

        # 거리 최소값 계산
        min_distance = float('inf')
        before = None
        for i in range(N):
            if seats[i] == 1:
                if before != None:
                    min_distance = min(min_distance, i-before)
                before = i

        candidates.append(min_distance)
        seats[N-1] = 0

    print(max(candidates))