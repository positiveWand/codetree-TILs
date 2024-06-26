N = int(input())
seats = list(map(int, list(input())))
occupied = [i for i in range(N) if seats[i] == 1]

# print(seats)
# print(occupied)

answer = 0
for i in range(N):
    if seats[i] == 1:
        continue
    
    closest_distance = float('inf')
    for j in range(len(occupied)):
        for k in range(j+1, len(occupied)):
            closest_distance = min(closest_distance, abs(occupied[j]-occupied[k]))
    for o in occupied:
        closest_distance = min(closest_distance, abs(o-i))
    
    answer = max(answer , closest_distance)

print(answer)