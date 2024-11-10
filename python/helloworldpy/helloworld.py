import conversations as hwconv
import algorithms as hwalgo
import datastructures as hwds
import ressourceman as resman
import os

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')  


print('Hello World!')
print("I'm running Python code on my own environment!\n")

while True:

    print('Available programs:')
    print('-------------------')
    print('1.  Name')
    print('2.  Age')
    print('3.  How are you?')
    print('4.  Bool test')
    print('5.  For loop over list')
    print('6.  For loop with range')
    print('7.  Recursion 1 - Factorial')
    print('8.  Recursion 2 - Fibonacci')
    print('9.  Recursion 3 - Binary Search Tree')
    print('10. Ressource Management via Context Manager Function')
    print('11. Ressource Management via Context Manager Class')

    print('--')
    print('Q.  Quit')
    print('-------------------')

    specified_inputs = '1-9 or Q'

    input1 = input(f'Please select ({specified_inputs}) ')

    if input1.lower() == 'q':
        break
    try:
        selection = int(input1)
        clearscreen()
    except:
        print('Only following inputs allowed:',specified_inputs)
        break

    if selection == 1:
        hwconv.get_name()

    elif selection == 2:
        hwconv.get_age()
    
    elif selection == 3:
        hwconv.how_are()

    elif selection == 4:
        hwds.bool_test()

    elif selection == 5:
        hwds.loop_with_list()

    elif selection == 6:
        hwds.loop_with_range()

    elif selection == 7:
        hwalgo.recursion1()

    elif selection == 8:
        hwalgo.recursion2()

    elif selection == 9:
        hwalgo.recursion3()

    elif selection == 10:
        resman.res_man_func()

    elif selection == 11:
        resman.res_man_class()

    print()
    user_input = input('Enter to continue, No, N, Q to quit: ')
    user_input = user_input.lower()
    if user_input in ['no', 'n', 'q', 'quit', 'exit']:
        break
    else:
        clearscreen()


