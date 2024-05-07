X = int(input())

current_distance = 0
current_speed = 1
current_time = 0
while current_distance < X:
    current_distance += current_speed
    current_time += 1
    
    if X >= current_distance + (current_speed+1)*(current_speed+2)/2:
        current_speed += 1
    elif X >= current_distance + (current_speed)*(current_speed+1)/2:
        current_speed += 0
    else:
        current_speed -= 1

print(current_time)