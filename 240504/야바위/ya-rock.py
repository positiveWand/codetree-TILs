N = int(input())

shuffle = [tuple(map(int, input().split())) for _ in range(N)]

max_point = 0
answer = None

for i in range(3):
    point = 0
    board = [False,False,False]
    board[i] = True

    # 셔플 진행
    for s in shuffle:
        a,b,c = s
        # a번 종이컵과 b번 종이컵 교환
        tmp = board[b-1]
        board[b-1] = board[a-1]
        board[a-1] = tmp

        # c번 종이컵 확인
        if board[c-1]:
            point += 1

    if max_point < point:
        answer = i+1

print(answer)