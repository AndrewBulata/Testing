## Pseudocode

# for variable in range(1, 10):
    # if variable <= 5:
        # print variable x '*'
    # else print (10 - variable) x '*'

## Solution

# Initiate for-loop
for variable in range(1, 10):
    # Use if-statement to print '*' 
    if variable <= 5:
        print(variable * '*')

    # Use else to print the mirror image about the midpoint 
    else:
        print( (10-variable) * '*' )