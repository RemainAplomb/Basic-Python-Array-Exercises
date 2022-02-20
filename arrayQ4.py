"""
    NAME : DIBANSA , RAHMANI P.
    COURSE-SECTION = BSCPE 2-2
    SUBJECT : DATA STRUCTURES AND ALGORITHM

    QUESTION 4 : Write a python program to get
    the number of occurrences specified element.
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

element_dic = {}
element_list = []
print ( MyArray )

# HERE WE WILL BE COUNTING THE NUMBER OF TIMES THE ELEMENTS OCCURED
for pi in range ( len ( integers) ) :
    if MyArray[pi] not in element_list :
        element_list.append( MyArray[pi] )
        element_dic[ MyArray[pi] ] = 0
    element_dic[ MyArray[pi] ] += 1

for pi in range ( len ( integers) ) :
    try:
        print ( " The element " , element_list[pi] , " occured " , element_dic[ element_list[pi] ] , " time(s). " )
    except:
        break


