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