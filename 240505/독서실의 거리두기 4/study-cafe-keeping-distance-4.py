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

        for p1 in occupied+[i,j]:
            for p2 in occupied+[i,j]:
                if p1 == p2:
                    continue
                closest_distance = min(closest_distance, abs(p1-p2))
        
        answer = max(answer , closest_distance)

print(answer)