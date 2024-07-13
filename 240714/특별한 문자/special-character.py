string = input()
count = {}
for c in string:
    if c not in count:
        count[c] = 0
    count[c] += 1

found = False
for key,value in count.items():
    if value == 1:
        print(key)
        found = True
        break
if not found:
    print('None')