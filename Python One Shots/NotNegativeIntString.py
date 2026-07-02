def is_non_negative_int (s):
    if s.isnumeric():
        if int(s)>=0:
            return True
    else :
        return False
    
print(is_non_negative_int("1729"))
print(is_non_negative_int("000001729"))
print(is_non_negative_int("0000")) #True

print(is_non_negative_int("17a9"))
print(is_non_negative_int("-1729"))
print(is_non_negative_int("12."))
print(is_non_negative_int("")) #False
