start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
all_the_fives=0

if start<0:
    for i in range(start,end+1):
        while i<-1:
            d=abs(i%10)
            i=i//10
            if d==5:
                all_the_fives+=1
                break

for i in range(start,end+1):
    while i>0:
        d=i%10
        i=i//10
        if d==5:
            all_the_fives+=1
            break