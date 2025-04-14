def are_mutually_reverse (a,b):
    d=0
    f=0
    while b>0:
        f=f*10
        d=b%10
        f=f+d
        b=b//10
    if a==f:
        return True
    else :
        return False
    
print(are_mutually_reverse(1234,4321))
print(are_mutually_reverse(1234,1234))
print(are_mutually_reverse(1334,1334))
print(are_mutually_reverse(1334,4331))
print(are_mutually_reverse(1234,4322))