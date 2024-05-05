N = int(input())
seats = list(map(int, list(input())))
occupied = [i for i in range(N) if seats[i] == 1]

# print(seats)
# print(occupied)

answer = 0
for i in range(N):
    for j in range(N):
        if seats[i]==1 or seats[j]==1:
            continue
        
        closest_distance = float('inf')
        for k in range(len(occupied)):
            for l in range(k+1, len(occupied)):
                closest_distance = min(closest_distance, abs(occupied[k]-occupied[l]))

        for o in occupied:
            closest_distance = min(closest_distance, abs(o-i))
            closest_distance = min(closest_distance, abs(o-j))
        
        answer = max(answer , closest_distance)

print(answer)