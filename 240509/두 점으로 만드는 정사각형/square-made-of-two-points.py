x1,y1,x2,y2 = list(map(int, input().split()))
a1,b1,a2,b2 = list(map(int, input().split()))

min_y = min(y1,y2,b1,b2)
max_y = max(y1,y2,b1,b2)
min_x = min(x1,x2,a1,a2)
max_x = max(x1,x2,a1,a2)

length = max((max_y-min_y), (max_x-min_x))

print(length**2)