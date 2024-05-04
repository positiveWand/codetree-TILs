import copy

board = [list(map(int, list(input()))) for _ in range(3)]
# print(board)

answer = 0
for i in range(1, 10):
    for j in range(i+1, 10):
        test = copy.deepcopy(board)
    
        for a in range(3):
            for b in range(3):
                if test[a][b] == i or test[a][b] == j:
                    test[a][b] = 0

        if test[0][0]==test[0][1]==test[0][2]==0\
        or test[1][0]==test[1][1]==test[1][2]==0\
        or test[2][0]==test[2][1]==test[2][2]==0\
        or test[0][0]==test[1][0]==test[2][0]==0\
        or test[0][1]==test[1][1]==test[2][1]==0\
        or test[0][2]==test[1][2]==test[2][2]==0\
        or test[0][0]==test[1][1]==test[2][2]==0\
        or test[0][2]==test[1][1]==test[2][0]==0:
            answer += 1

print(answer)