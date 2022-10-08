import input as inp

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def recursion1():
    num_int = inp.input_number()
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
    num_int = inp.input_number()
    if num_int == -1:
        print('Wrong input.')
        return

    print(fibonacci(num_int))

def build_bst(list):
  if len(list) == 0:
    return "No Child"
  middle_idx = len(list) // 2
  middle_value = list[middle_idx]
  left_half = list[0:middle_idx]
  right_half = list[middle_idx+1:]
  bst_node = { "data": middle_value }
  bst_node["left_child"] = build_bst(left_half)
  bst_node["right_child"] = build_bst(right_half)
  return bst_node
  
def recursion3():
    num_list = [1,3,14,35,66,78,98,101,123,133,155,199,205,255,512,640,768,1024]
    num_list.sort
    print(build_bst(num_list))