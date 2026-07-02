from math import *

a = float(input('enter number :'))
op = input('enter operation :')
b = float(input('enter number :'))

if (op == '+')  or (op == '-') or (op == '/') or (op == '*'):
    
    if op =='+':   
        r= a+b
        print('%s %s %s = %s' % (a,op,b,r))

    elif op =='-':
        r= a-b
        print('%s %s %s = %s' % (a,op,b,r))
    
    elif op =='/':
        r= a/b
        print('%s %s %s = %s' % (a,op,b,r))
    
    elif op =='*':
        r= a*b
        print('%s %s %s = %s' % (a,op,b,r))
    
elif (op == '#') or (op == '^') or (op == '%') or (op == 'b')  : 

    if op =='#':   
            r= a**(1/b)
            print('%s %s %s = %s' % (a,op,b,r))

    elif op =='^': 
            r= a**b
            print('%s %s %s = %s' % (a,op,b,r))
        
    elif op =='%':  
            r= a%b
            print('%s %s %s = %s' % (a,op,b,r))
        
    elif op =='b': 

            # a = int(a)
            # b = int(b)
            # r = int(str(a),b)
            # r = int2base(a,b) 
            # print('%s %s %s = %s' % (a,op,b,r))

        if b == 2 :    
            r= bin(int(a)) 
            print('%s %s %s = %s' % (a,op,b,r))
        elif b == 8 :    
            r= oct(int(a)) 
            print('%s %s %s = %s' % (a,op,b,r))
        elif b == 16 :    
            r = hex(int(a))
            print('%s %s %s = %s' % (a,op,b,r))
        else :
            print('base not supported')    
        
else:
 print('wrong operation input')