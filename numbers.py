# Take 3 numbers as input from user

integers = int(input('Number 1: ')), int(input('Number 2: ')), int(input('Number 3: '))

# Print the sum of all 3 numbers
print('The sum is: ', sum(integers))

# Print the first number minus the second number
print('Difference: ', integers[0] - integers[1])

# Print the third number multiplied by the first number
print('The third number multiplied by the first number: ', integers[2] * integers[0])

# Print the sum of all three numbers divided by the third number
print('The sum of all three numbers divided by the third number: ', sum(integers)/integers[2])