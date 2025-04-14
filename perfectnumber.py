n = 10000

for i in range(1, n+1):
    j = 1
    total = 0
    while j < i:
        if i % j == 0:
            total += j
        j += 1

    if i == total:
        print(i)

