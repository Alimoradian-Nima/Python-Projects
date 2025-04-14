theString = input("Enter a string: ")
count=0 
x = len(theString)
for i in range (x-1):
        if theString[i]==theString[i+1] and theString[i].isalpha() and theString[i+1].isalpha():
            count=count+1
print(count)