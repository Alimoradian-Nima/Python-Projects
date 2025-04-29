num_students = 5
n = ""
while num_students > 0:
    print(n,"\o/ <this exam is so fun!>")
    n = n+" "
    num_students -= 1
print("student line")

num_students = 5
for i in range(1, num_students):
    spaces = " " * (num_students - i -1)  # Add spaces for alignment
    row = "\\o/" * i  # Create the row with the correct number of \o/
    row = row + "\\o/"
    print(spaces + row)  # Print the aligned row

print("student pyramid")

for i in range(6):
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(7,0,-1):
    for j in range(i):
        print("#",end="")
    print()

for i in range(7,0,-1):
    line=""
    for j in range (i):
        line=line+"#"
    print(line)

n =5
for i in range(n):
    line=""
    for j in range(i+1):
        line=line+"& "
    print(line)

for n in range(n,0,-1):
    for j in range(n):
        print("!- ",end="")
    print()

def cat(n):
    for i in range(n):
        for j in range(0,i+1):
            print(j*2,end=' ')
        print()

cat(5)

def triangle1 (n):
    for i in range (1,n+1):
        print('*'*i)

triangle1(5)

def triangle2 (n):
    for i in range(1,n+1):
        print(" "*(n-i)+'#'*i)

triangle2(5)

def diamond (n):
    for i in range(1,2*n):
        if i<=n:
            print(' '*(n-i)+'*'*(i)+'*'*(i-1))
        if i>n:
            print(' '*(i-n)+'*'*(2*n-i)+'*'*((2*n-1)-i))

diamond(5)
diamond(10)