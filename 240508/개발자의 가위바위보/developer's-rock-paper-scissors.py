N = int(input())
games = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0
for rock, scissor, paper in [(1,2,3),(2,1,3),(3,2,1),(1,3,2),(3,1,2),(2,3,1)]:
    wins = 0
    for game in games:
        if game[0]==rock and game[1]==scissor\
        or game[0]==scissor and game[1]==paper\
        or game[0]==paper and game[1]==rock:
            wins += 1
    
    answer = max(answer, wins)

print(answer)