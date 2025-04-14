# #Fibonacci sequence
# def fibonacci(n):
#     """Return the Fibonacci sequence up to n."""
#     fib_sequence = []
#     a, b = 0, 1
#     while a < n:
#         fib_sequence.append(a)
#         a, b = b, a + b
#     return fib_sequence

n = int(input("Enter a number: "))
a =0
b = 1
c = 0
while c < n:
    c = a + b
    a = b
    b = c
    print(c)
