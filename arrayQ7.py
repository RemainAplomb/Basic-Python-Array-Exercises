"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM

    QUESTION 7 : Write a python program to remove the
    first occurrence of a specified element
    
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

# WE WILL BE ASKING THE USER WHAT INTEGER HE WANTS TO REMOVE
rem_int = int ( input ( " Enter the integer that you want to remove it's first occurence : " ) )

# HERE WE WILL TRY TO REMOVE THE USER'S INPUTTED INTEGER
try:
    MyArray.remove ( rem_int )
except: # IF THE INTEGER CANNOT BE FOUND WITHIN THE LIST , WE WILL BE PRINTING AN ERROR
    print ( " The integer that you've entered can't be found. " )

print ( " \n\n " )
print ( MyArray )
