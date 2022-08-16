def get_name():
    name = input("What's your name? ")

    print(f'Hello {name}, how nice to meet you.')
    print('Your name was saved in a variable of type', type(name))

def get_age():
    age_str = input('How old are you? ')
    age_int = int(age_str)

    if age_int == 42:
        print('42 is also the answer to the Ultimate Question of Life, the Universe, and Everything. :-)')

    else:
        print(f'{age_int} is a great age!')

    print(f'Your age was converted to and saved in a variable of data type {type(age_int)}.')

def how_are():
    how_are_you = input('How are you? ')
    if how_are_you == 'Bad':
        print("I'm sorry to hear that.")
    else:
        response = '{} sounds fine!'
        print(response.format(how_are_you))

def bool_test():
    truthy = bool('Hello world')  # Always true unless empty, 0, none or false
    print('This variable is',truthy)

def loop_with_list():
    world_championships = [1954, 1974, 1990, 2014]
    print('Germany became football world champion in:')
    for year in world_championships:
        print(year)

def loop_with_range():
    for i in range(5):
        print(i)    

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def input_number():
    num_str = input('Input positive number: ')
    try:
        num_int = int(num_str)
        if num_int <= 0:
            return -1
        else:
            return num_int
    except:
        print(f'{num_str} is not a number.')
        return -1

def recursion1():
    num_int = input_number()
    if num_int == -1:
        print('Wrong input.')
        return
    else:
        print(factorial(num_int))

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def recursion2():
    num_int = input_number()
    if num_int == -1:
        print('Wrong input.')
        return

    print(fibonacci(num_int))


print('Hello World!')
print("I'm running Python code on my own environment!")

while True:

    print()
    print('Available programs:')
    print('-------------------')
    print('1. Name')
    print('2. Age')
    print('3. How are you?')
    print('4. Bool test')
    print('5. For loop over list')
    print('6. For loop with range')
    print('7. Recursion 1 - Factorial')
    print('8. Recursion 2 - Fibonacci')
    print('--')
    print('Q. Quit')
    print('-------------------')

    specified_inputs = '1-8 or Q'

    input1 = input(f'Please select ({specified_inputs}) ')

    if input1.lower() == 'q':
        break

    try:
        selection = int(input1)
    except:
        print('Only following inputs allowed:',specified_inputs)
        break

    if selection == 1:
        get_name()

    elif selection == 2:
        get_age()
    
    elif selection == 3:
        how_are()

    elif selection == 4:
        bool_test()

    elif selection == 5:
        loop_with_list()

    elif selection == 6:
        loop_with_range()

    elif selection == 7:
        recursion1()

    elif selection == 8:
        recursion2()

    print()
    user_input = input('One more time? (Yes or Y) ')
    user_input = user_input.lower()
    if user_input == 'yes' or user_input == 'y':
        # Continues for or while loop without doing anything
        # Difference to continue is that continue would immediately
        # go to the next iteration while pass does not do anything. 
        # This is needed as in python for loops can not be empty
        pass  
    else:
        break


