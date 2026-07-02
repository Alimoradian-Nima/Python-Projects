# if 5>3:
#     print("this is amazing")

x = int(input("Enter a number: "))

# if x>0:
#     print("x is Positive")
# elif x<0:
#     print("x is Negative")
# else:
#     print("x is Zero")

# if x%2 == 0:
#     print("x is Even")
# elif x%3 == 0 and x%2 != 0:
#     print("x is Odd\nx is Divisible by 3")
# elif x%3 == 0:
#     print("x is Divisible by 3")
# else:
#     print("x is Odd")

# if x > 3:
#     x = x * 2
#     if x == 3:
#         x = x + 5
#         if x % 2 == 0:
#             x = 4
#         else:
#             x = x * 4
# elif x < 0:
#     if x % 2 == 0:
#         x = x + 1
#     elif x == 15:
#         x = x - 1
#     x = x + 6
# else:
#     x + 1
#     if x == 3:
#         x = x + 2
#     else:
#         x = x + 10
#     x = x + 50

# print(x)

# x = True # x is less than 5

#chech if x is a number
if type(x) == int:
    if x >5:
        print("x is greater than 5")

    elif x == 5:
        print("x is equal to 5")

    else:
        print("x is less than 5")
else:
    print("x is not a number")