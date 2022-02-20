"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM

    QUESTION 3 : Write a python program to reverse
    the order of the items in the array.
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

print ( " This is the original order of the array. " )

print ( MyArray )

# WE WILL BE REVERSING THE ARRAY
MyArray.reverse()

print ( " This is the reversed order of the array. " )

print ( MyArray )
