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