def print_pattern(n):
    for i in range(n, 0, -1):
        line = ""
        for j in range(0, i):
            j = j*2
            line += str(j)
        print(line)

print_pattern(4)
