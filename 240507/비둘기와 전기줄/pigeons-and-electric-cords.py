N = int(input())
piegeons = [None for _ in range(11)]

answer = 0
for i in range(N):
    piegeon, where = tuple(map(int, input().split()))
    if piegeons[piegeon] == None:
        piegeons[piegeon] = where
    elif piegeons[piegeon] != where:
        answer += 1
        piegeons[piegeon] = where

print(answer)