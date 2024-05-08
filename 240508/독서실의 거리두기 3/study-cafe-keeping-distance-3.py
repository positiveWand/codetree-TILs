N = int(input())
seats = list(map(int, list(input())))

# 가장 가까운 2개 위치 계산
furthest = None
max_distance = 0
before = 0
for i in range(N):
    if i != 0 and seats[i] == 1:
        if  max_distance < i-before:
            max_distance = i-before
            furthest = (before, i)
        before = i

# print(max_distance)
# print(furthest)

seats[(furthest[1]+furthest[0])//2] = 1
# print(seats)



# 거리 최소값 계산
min_distance = float('inf')
before = 0
for i in range(N):
    if i != 0 and seats[i] == 1:
        min_distance = min(min_distance, i-before)
        before = i

print(min_distance)