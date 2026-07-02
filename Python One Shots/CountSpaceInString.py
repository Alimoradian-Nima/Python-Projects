def count_spaces (s:str):
    space_count=0
    # for i in range(len(s)):
    #     if s[i]==" ":
    for ch in s:
        if ch==" ":
            space_count+=1
    return space_count

count_spaces("hello world")
print(count_spaces("he ll o wor ld "))