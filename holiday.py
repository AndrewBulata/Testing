## Holiday Cost

# Create a function that takes in multiple inputs: cities:
        # we take inot consideration 3 cities

def multiple_choice_input(prompt, options):
    while True:
        print(prompt)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1]
        
        print("Invalid choice. Please enter a number corresponding to one of the options.")

city_options = ["New York", "London", "Paris"]
chosen_city = multiple_choice_input("Choose a city:", city_options)
print("You chose:", chosen_city)



