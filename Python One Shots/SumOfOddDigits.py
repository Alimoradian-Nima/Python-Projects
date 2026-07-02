value=int(input("Enter a number: "))
odd_digits_sum=0
if value<0:
    value=-value
while value>0:
    d=value%10
    if d%2!=0:
        odd_digits_sum+=d
    value=value//10
print(odd_digits_sum)