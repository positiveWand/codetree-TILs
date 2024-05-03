N,C,G,H = list(map(int, input().split()))
temp_range = [list(map(int, input().split())) for _ in range(N)]

temp_min = min(temp_range, key=lambda x: x[0])[0]
temp_max = max(temp_range, key=lambda x: x[1])[1]

# print(temp_range)
# print(temp_min)
# print(temp_max)

answer = 0
for temp in range(max(0, temp_min-1), temp_max+1):
    productivity = 0
    for temp_start, temp_end in temp_range:
        if temp < temp_start:
            productivity += C
        elif temp_start <= temp <= temp_end:
            productivity += G
        else:
            productivity += H
    
    answer = max(productivity, answer)

print(answer)