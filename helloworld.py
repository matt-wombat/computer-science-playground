print('Hello World!')
print("I'm running Python code on my own environment!")

one_more_loop = True

while one_more_loop:

    print()
    print('Available programs:')
    print('-------------------')
    print('1. Name')
    print('2. Age')
    print('3. How are you?')
    print('4. Bool test')
    print('5. For loop over list')
    print('6. For loop with range')
    print('-------------------')
    selection = int(input('Please select (1-5) '))

    if selection == 1:
        name = input("What's your name? ")

        print(f'Hello {name}, how nice to meet you.')
        print('Your name was saved in a variable of type', type(name))

    elif selection == 2:
        age_str = input('How old are you? ')
        age_int = int(age_str)

        print(f'{age_int} is a great age!')
        print(f'Your age was converted to and saved in a variable of data type {type(age_int)}.')
    
    elif selection == 3:
        how_are_you = input('How are you? ')
        if how_are_you == 'Bad':
            print("I'm sorry to hear that.")
        else:
            response = '{} sounds fine!'
            print(response.format(how_are_you))

    elif selection == 4:
        truthy = bool('Hello world')  # Always true unless empty, 0, none or false
        print('This variable is',truthy)

    elif selection == 5:
        world_championships = [1954, 1974, 1990, 2014]
        print('Germany became football world champion in:')
        for year in world_championships:
            print(year)

    elif selection == 6:
        for i in range(5):
            print(i)

    print()
    user_input = input('One more time? (Yes or Y) ')
    user_input = user_input.lower()
    if user_input == 'yes' or user_input == 'y':
        one_more_loop = True
    else:
        one_more_loop = False




