"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM

    QUESTION 8 :Write a python program to convert an array to an ordinary list.
    
"""

"""
   First we will need to import array.
"""

import array as asArray

"""
   Here we will be asking the user for the integers that he want to put in
   the array.
"""

integers = eval ( input ( " Enter the integers you want to put inside your array : " ) )

"""
   Then, we will create an array that contains the user's integers.
"""
MyArray = asArray.array ( "i" , integers )

arrayInList = []
print ( MyArray )

# HERE WE WILL CONVERT THE ARRAY INTO A LIST
for pi in range ( len ( integers) ) :
    arrayInList.append ( MyArray [pi] )

print ( " The array has been successfully converted. " )
print ( arrayInList )
    
