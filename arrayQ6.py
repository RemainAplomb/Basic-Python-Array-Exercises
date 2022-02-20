"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM

    QUESTION 6 : Write a python program to remove the third item.
    
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

# HERE WE WILL BE REMOVING THE SECOND ITEM WITHIN THE LIST
MyArray.pop(2)

print ( " \n\n" )
print ( " The third item has been removed. " )

print ( MyArray )
