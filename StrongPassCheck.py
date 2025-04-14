def classify_password (s):
    if not s: #or not s.strip(): 
        return "Password is empty"
    if len(s)<8:
        return "Password too short"
        
    has_uppercase=False
    has_digit=False
    for char in s:
        if 'A' <= char <= 'Z': # Check if the character is uppercase
            has_uppercase = True
        elif char.isdigit(): # Check if the character is a digit (0-9)
            has_digit = True
     
        if has_uppercase and has_digit:
            break
        
    if not has_uppercase:
        return "Password must contain at least one uppercase letter"

    if not has_digit:
        return "Password must contain at least one digit"
    
    elif has_uppercase and has_digit: 
        return "Password is strong"
        

print(classify_password("frog")) #Password too short
print(classify_password("")) #Password is empty
print(classify_password("Datadatadata")) #Password must contain at least one digit
print(classify_password("8atadatadata")) #Password must contain at least one uppercase letter
print(classify_password("Data88adata")) #Password is strong