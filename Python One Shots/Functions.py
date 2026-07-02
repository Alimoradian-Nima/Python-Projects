# def Function1():
#     # Function 1 code here
#     print("Function 1 executed")
#     return 2
# Function1()
# print(Function1())

# #Define a function foo that prints "Hello World"
# def foo():
#     print("Hello World")
# #Call the function foo
# print(foo())
# #Define a function bar that prints "How are you doing today?"
# def bar():
#     print("How are you doing today?")
# #Call the foo and bar functions
# foo()
# bar()

# bar()
# foo()

# #Write a function named is_greater_than that takes 2 values and returns True if the first value is larger than second value, False otherwise.
# def is_greater_than(a, b):
#     if a > b:
#         return True
#     else:
#         return False

# #Write a function named get_average that takes 3 values and returns the average of the three values.
# import math
# import statistics
# def get_average(a, b, c):
#     #return (a + b + c) / 3
#     return statistics.mean([a, b, c])

# is_greater_than(5, 5)
# is_greater_than(5, 6)
# is_greater_than(0, -1)
# get_average(5, 5, 5)
# get_average(5, 6, 7)
# get_average(5.1, 5.2, 5.3)

# print(is_greater_than(5, 5))
# print(is_greater_than(5, 6))
# print(is_greater_than(0, -1))
# print(get_average(5, 5, 5))
# print(get_average(5, 6, 7))
# print(get_average(5.1, 5.2, 5.3))

def numberOfDaysInGregorianMonth( month, year ):
    if type(month) != int or type(year) != int or year == 0 or month < 1 or month > 12:
        return 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28
        # if year % 4 == 0:
        #     return 29
        # if year % 100 == 0:
        #     return 28
        # if year % 400 == 0:
        #     return 29
        # if year % 4 != 0:
        #     return 28
        
numberOfDaysInGregorianMonth( 2, 2000 ) # testing for:  February in a leap year that is divisible by 400
numberOfDaysInGregorianMonth( 2, 1999 ) # testing for:  February in a a non-leap year that is not divisible by 4.

for j in range(1960, 2101, 30):
    for i in range(1, 13):
        print(i,j,numberOfDaysInGregorianMonth( i, j )) # testing for:  February in a leap year that is divisible by 400    