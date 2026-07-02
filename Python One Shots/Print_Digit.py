import math
n = int(input("enter a number :" ))

#take the number n and print the left most digit of the number
print(n//(10**(len(str(n))-1)))

print(n//(10**math.floor(math.log10(n))))

#take the number n and print the second to last digit of the number
print((n % 100) // 10)
