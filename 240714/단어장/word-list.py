n = int(input())
count = {}
for _ in range(n):
    string = input()
    if string not in count:
        count[string] = 0
    count[string] += 1

for key in sorted(count.keys()):
    print(key, count[key])