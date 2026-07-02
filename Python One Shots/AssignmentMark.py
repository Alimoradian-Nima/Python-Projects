assignmentMark = 6.5

assignmentMarkedOutOf = 9

percentage = (assignmentMark/assignmentMarkedOutOf)*100
print(percentage)
percentage= 101


if percentage < 50:
    print ("F")
elif percentage >= 50 and percentage<65:
    print ("Pass")
elif percentage >= 65 and percentage<75:
    print ("Credit")
elif percentage >= 75 and percentage<85:
    print ("Distinction")
elif percentage >= 85 and percentage<=100:
    print ("High Distinction")
elif percentage < 0 or percentage> 100:
    print ("error")
else :
    print ("Error")