## Outline

# 1. Collect input from user
    # user_name = insert name
    # user_age = insert age
    # user_house_number = insert house number
    # user_street_name = insert street name

# 2. Print final message
   # This is {user_name}. He is {user_age} years old and lives at house number {user_house_number} on {user_street_name}.


## Solution

# Step 1: Collect input from user
user_name = input('Insert your name ')
user_age = int(input('Insert you age ')) #use int() on input() to take integers
user_house_number = input('Insert your house number ')
user_street_name = input('Insert your street name ')

# Step 2: Print final message
print(f"This is {user_name.capitalize()}. He is {user_age} years old and lives at house number {user_house_number} on {user_street_name.capitalize()}.")
#adding .capitalize() to esure neat output irrespective of user input
