shift = 3
theString = "Abc? dEF.ghi_Jkl-MnoP!...Xyz"
newString = ""
shift = shift % 26 # To handle shifts greater than 26
for char in theString:
    if char.isalpha():
         if ord(char) + shift > ord('Z') and char.isupper():
            new_char = chr(ord(char) - 26 + shift)
            newString+=new_char
         elif ord(char) + shift > ord('z') and char.islower():
            new_char = chr(ord(char) - 26 + shift)
            newString+=new_char
         else:
            new_char = chr(ord(char) + shift)
            newString+=new_char
    else:
        newString+=char
print(newString)
