def is_prime (a):
    # flag=True
    if a<2:
        # flag=False
        return False
    elif a==2:
        # flag= True
        return True
    for i in range (2,a):
        if a%i==0:
            # flag= False
            return False

    # return flag
    return True

print(is_prime(2)) # True  
print(is_prime(3)) # True
print(is_prime(4)) # False
print(is_prime(5)) # True
print(is_prime(100003)) # True
print(is_prime(100007)) # Flase
print(is_prime(91)) # False
print(is_prime(47)) # True
print(is_prime(49)) # False
print(is_prime(1)) # False
print(is_prime(93)) # False
print(is_prime(89)) # True