import array as asArray

integers = eval ( input ( " Enter the integers you want to put inside your array : " ) )

integers2 = list ( integers )
integers2.sort()

MyArray = asArray.array ( "i" , integers )
MyArrayBinary = asArray.array ( "i" , integers2 )

searchNum = eval ( input ( " Enter the integer that you would like to search for : " ) )

# Linear

print ( " Your Linear Array : " , end = " " )
for i in range ( len ( MyArray) ):
    print ( MyArray[i] , end = " " )
print ( "" )
for i in range ( len ( MyArray) ) :
    if searchNum == MyArray[i] :
        print ( " The index of " , searchNum , " is " , i , "." )
        break

# Binary
print ( " Your Binary Array : " , end = " " )
for i in range ( len ( MyArrayBinary) ):
    print ( MyArrayBinary[i] , end = " " )
print ( "" )

high = int ( MyArrayBinary[ len ( MyArrayBinary ) - 1 ] )
low = searchNum

mid = int (( high - low ) / 2 )
temp = str( mid )
mid = int ( temp[0] )

found = False

while found == False:
    print ( mid )
    if MyArrayBinary[mid] == searchNum:
        print ( " The index of " , searchNum , " is " , mid )
        found = True
    elif MyArrayBinary[mid] > searchNum:
        print ( ">" )
        mid  -= 1
    elif MyArrayBinary[mid] < searchNum:
        print ( "<" )
        mid += 1


