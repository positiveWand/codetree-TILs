n = int(input())
chars = input().split()

# print(chars)
answer = 0
for i, char in enumerate(sorted(chars)):
    current = chars.index(char)
    for _ in range(current-i):
        chars[current], chars[current-1] = chars[current-1], chars[current]
        current -= 1
        answer += 1

print(answer)