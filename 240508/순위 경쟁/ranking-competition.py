n = int(input())

change = []
for _ in range(n):
    t = input().split()
    change.append((t[0],int(t[1])))

answer = 0
score = {'A':0, 'B':0, 'C':0}
scoreboard = set(['A','B','C'])
for s, c in change:
    score[s] += c
    new_scoreboard = set()
    if max(score.values()) == score['A']:
        new_scoreboard.add('A')
    if max(score.values()) == score['B']:
        new_scoreboard.add('B')
    if max(score.values()) == score['C']:
        new_scoreboard.add('C')
    
    if new_scoreboard != scoreboard:
        answer += 1
    
    scoreboard = new_scoreboard

print(answer)