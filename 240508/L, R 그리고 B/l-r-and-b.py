board = [
    list(input())
    for _ in range(10)
]

# print(board)

l_pos = None
r_pos = None
b_pos = None
for i in range(10):
    for j in range(10):
        if board[i][j] == 'B':
            b_pos = (i,j)
        if board[i][j] == 'L':
            l_pos = (i,j)
        if board[i][j] == 'R':
            r_pos = (i,j)
# print(l_pos, r_pos, b_pos)

distance = None
if l_pos[0]==r_pos[0]==b_pos[0]:
    distance = abs(l_pos[1]-b_pos[1])+1
    # print('x')
elif l_pos[1]==r_pos[1]==b_pos[1]:
    distance = abs(l_pos[0]-b_pos[0])+1
    # print('y')
else:
    distance = abs(l_pos[0]-b_pos[0])+abs(l_pos[1]-b_pos[1])-1

print(distance)