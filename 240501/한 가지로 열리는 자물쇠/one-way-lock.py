N = int(input())

combination = list(map(int, input().split()))

answer = 0

for first in range(1,N+1):
    for second in range(1,N+1):
        for third in range(1,N+1):
            if abs(combination[0] - first) <= 2\
            or abs(combination[1] - second) <= 2\
            or abs(combination[2] - third) <= 2:
                answer += 1

print(answer)