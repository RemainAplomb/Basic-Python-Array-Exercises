"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM

    QESTION 1 : Write a python program to create an array of five
    integers and display the array items, access individual element and indices.
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

"""
   Lastly, we will access and print the data within the created array.
"""
for pi in range ( len ( integers) ) :
    print ( " Index number " , pi , " : " , end = " " )
    print ( MyArray[ pi ] )



