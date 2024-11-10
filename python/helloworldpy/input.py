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
