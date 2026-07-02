def soup (s):
    reverse_string=""
    for i in range(len(s),0,-1):
        reverse_string=reverse_string+s[i-1]
    print(reverse_string)

soup("hello")
soup("hello world")