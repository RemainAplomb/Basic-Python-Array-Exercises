"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM

    QUESTION 5 :Write a python program to insert a new
    item before the second element in an existing array.
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

# WE WILL ASK THE USER FOR AN INTEGER TO INSERT
insert_int = int ( input ( " Enter an integer that you want to insert : " ) )

# WE WILL INSERT THE INTEGER INTO THE SECOND SLOT OF THE ARRAY
MyArray.insert( 1 , insert_int )

print ( MyArray )
