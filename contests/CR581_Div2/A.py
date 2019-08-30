s = int(input(), 2)
count = 0
for i in range(0, 2**100):
    if 4**i < s:
        count += 1
    else:
        break
print(count)
