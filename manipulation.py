
# Take input from user
str_manip = input('Please enter your sentence here ')
str_manip = str_manip.strip()

# Calculate and print the length of the sentence
print(f'The sentence is {len(str_manip)} characters long.')

# Find the last character and define it
if str_manip[-1] != '.':
    char = str_manip[-1]
    print(f"The last character is {char}.")
else:
    char = str_manip[-2]
    print(f"The last character is {char}.")

# Replace the last character and all its occurences with '@'
    # use a for-loop to scan the sentence
new_sentence = ''     
for u in str_manip:
    if u == char:
        u = '@'
    new_sentence += u

print(new_sentence)

# More interesting method
print(str_manip.replace(char, '@'))


# Print last three characters backwards, this time without the use of if-statements
str_manip = str_manip.strip(",.")
charr = str_manip[-3:]


print('Reverse string: ', charr[::-1])

#Create a five-letter word that is made up of the first three characters and the last two characters in str_manip.
print(str_manip[:3] + str_manip[-2:])