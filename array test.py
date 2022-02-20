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

import array as arruy_inday

"""
   Here we will be asking the user for the integers that he want to put in
   the array.
"""

n1 = int ( input ( " Enter the first integer that you want : " ) )
n2 = int ( input ( " Enter the second integer that you want : " ) ) 
n3 = int ( input ( " Enter the third integer that you want : " ) )
n4 = int ( input ( " Enter the fourth integer that you want : " ) )
n5 = int ( input ( " Enter the fifth integer that you want : " ) )


"""
   Then, we will create an array that contains the user's integers.
"""
arruy = arruy_inday.array ( "i" , [ n1 , n2 , n3 , n4 , n5 ] )

"""
   Lastly, we will access and print the data within the created array.
"""
for pi in range ( 5 ) :
    print ( arruy[ pi ] )


