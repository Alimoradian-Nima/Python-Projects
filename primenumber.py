def ulist (inlist):
    unique = []
    for n in inlist :
        if n not in unique :
            unique.append(n)
    #print("unique",unique)
    return unique
    #return list(set(inlist))

def prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

def main ():
    ui = input("Enter a list:" )
    ui = ui.strip('[]')  # Remove the square brackets
    ui = [int(num) for num in ui.split(',') if num.strip().isdigit()]
    #print("ui", ui)
    # ui = [1,2,2,3,4,5,5,5,6,7,8,9]
    ul = ulist(ui)
    #print('ul',ul)
    r = [n for n in ul if prime(n)]
    print(r)


main()