## Pseudocode

# declare condition
# while condition
    # take input
        # if input not = -1
            # add input to list 
        # if input = -1
            # stop
            # sum list

## Solution

# Initialise empty list
inputs = []

# Apply condition
while True:
    
    # Take user input
    user_input = float(input('Type in a number: '))
    
    # Use conditionals
    if user_input != -1:
        # Add numbers to the pre-defined list
        inputs.append(user_input)
    else:
        # Print sum and break the loop
        print(sum(inputs))
        break
        




