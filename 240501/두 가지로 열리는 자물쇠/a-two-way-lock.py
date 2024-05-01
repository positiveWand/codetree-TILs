N = int(input())

first_combi = tuple(map(int, input().split()))
second_combi = tuple(map(int, input().split()))

answer = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            first = False
            if min(abs(first_combi[0]-i), N-abs(first_combi[0]-i)) <= 2\
            and min(abs(first_combi[1]-j), N-abs(first_combi[1]-j)) <= 2\
            and min(abs(first_combi[2]-k), N-abs(first_combi[2]-k)) <= 2:
                first = True
            
            second = False
            if min(abs(second_combi[0]-i), N-abs(second_combi[0]-i)) <= 2\
            and min(abs(second_combi[1]-j), N-abs(second_combi[1]-j)) <= 2\
            and min(abs(second_combi[2]-k), N-abs(second_combi[2]-k)) <= 2:
                second = True
            
            if first or second:
                answer += 1

print(answer)