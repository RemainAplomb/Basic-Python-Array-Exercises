"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM

    QESTION 2 : Write a python program to append a
    new item to the end of the array
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


print ( MyArray )

appendINT = int ( input ( " What do you want to append to the array? " ) )

# WE WILL APPEND THE INTEGER TO THE ARRAY
MyArray.append( appendINT )

print ( MyArray )
