myString = "abcdefghijklmnop"
print( "line 1-" + myString[ : : ] ) # prints the whole string no conditions
print( "line 2-" + myString[5 : 2] ) # prints nothing because the start index is greater than the end index
print( "line 2.5-" + myString[5 : 1:-2] )
print( "line 3-" + myString[5 : -2] ) # prints the string from index 5 to the second last index
print( "line 4-" + myString[5 : 6] )
print( "line 5-" + myString[5 : 12] )
print( "line 6-" + myString[1 : : 2] ) # prints the string from index 1 to the end with a step of 2
print( "line 7-" + myString[1 : : 3] )
print( "line 8-" + myString[ : : 2] )
print( "line 9-" + myString[ : : 3] )

myString = "abcdefghijklmnop"
print( "line 10-" + myString[ : : -1 ] ) # prints the string in reverse order
