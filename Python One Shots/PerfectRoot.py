import math
def is_perfect_square (n):
    if n>=0:
        if int(math.sqrt(n))**2 == n:
            return True
        else :
            return False
    else :
        return False
    
print(is_perfect_square(49)) # True
print(is_perfect_square(65536)) # True
print(is_perfect_square(50)) # False
print(is_perfect_square(65535)) # False
print(is_perfect_square(-1)) # False
print(is_perfect_square(1530169)) # True
print()

def is_perfect_cube(n):
    for i in range(0,n//2+1):
        if i*i*i ==n:
            return True
    return False

print(is_perfect_cube(8)) # True
print(is_perfect_cube(1000000)) # True
print(is_perfect_cube(70000)) # False
print(is_perfect_cube(80)) # False
print(is_perfect_cube(-1)) # False
print(is_perfect_cube(1860867)) # True