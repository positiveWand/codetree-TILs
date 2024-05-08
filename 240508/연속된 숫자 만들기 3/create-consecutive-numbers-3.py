line = list(map(int, input().split()))

print(max(0, line[1]-line[0]-1, line[2]-line[1]-1))