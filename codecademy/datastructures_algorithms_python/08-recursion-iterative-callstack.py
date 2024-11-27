#
# Before we dive into recursion, let’s replicate what’s happening in the call 
# stack with an iterative function.
#
# The call stack is abstracted away from us in Python, but we can recreate it to
# understand how recursive calls build up and resolve.
#
# Let’s write a function that sums every number from 1 to the given input.
#
# To depict the steps of a recursive function, we’ll use a call stack and
# execution contexts for each function call.
#
# The call stack stores each function (with its internal variables) until those 
# resolve in a last in, first out order.
#
# Execution contexts are a mapping between variable names and their values 
# within the function during execution. We can use a list for our call stack 
# and a dictionary for each execution context.
#

def sum_all_numbers(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")

  while call_stack:
    return_value = call_stack[len(call_stack)-1]
    call_stack.pop(len(call_stack)-1)
    print(call_stack)
    print("Adding", str(return_value), "to", result)
    result += return_value['n_value']

  return result, call_stack

print("Result:", sum_all_numbers(4))