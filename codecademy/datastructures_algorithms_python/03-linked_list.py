class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node


class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

  def insert_beginning(self, new_value):
    print(f'Inserting at beginning {new_value}')
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

  def print(self):
    string = "(head) "
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value():
        if current_node != self.get_head_node():
          string += " -> "
        string += str(current_node.get_value())
      current_node = current_node.get_next_node()
    print("Linked list:", string, "(tail)")

  def remove_node(self, value_to_remove):
    print(f'Removing {value_to_remove}')
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

  def swap_nodes(self, val1, val2):
    print(f'Swapping {val1} with {val2}')

    node1 = self.head_node
    node2 = self.head_node
    node1_prev = None
    node2_prev = None

    # Find val1 and val2 in linked list 
    # and note prev-node
    while node1 is not None:
      if node1.get_value() == val1:
        break
      node1_prev = node1
      node1 = node1.get_next_node()

    while node2 is not None:
      if node2.get_value() == val2:
        break
      node2_prev = node2
      node2 = node2.get_next_node()

    # Check for edge cases
    if (node1 is None or node2 is None):
      print("Swap not possible - one or more element is not in the list")
      return

    if val1 == val2:
      print("Elements are the same - no swap needed")
      return

    # Change next node of previous node to the
    # new node, except previous node is None. 
    # In this case change list's head_node to the new node
    if node1_prev is None:
      self.head_node = node2
    else:
      node1_prev.set_next_node(node2);
    
    if node2_prev is None:
      self.head_node = node1
    else:
      node2_prev.set_next_node(node1);

    # Change next node of both swapped nodes
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)    


  def nth_last_node(self, n):
    nth_pointer = None
    tail_pointer = self.get_head_node()
    count = 1

    while tail_pointer:
      tail_pointer = tail_pointer.get_next_node()
      count += 1

      if count >= n + 1:
        if nth_pointer == None:
          nth_pointer = self.get_head_node()
        else:
          nth_pointer = nth_pointer.get_next_node()

    print(f'{n} to last is {nth_pointer.get_value()}')
  

  def find_middle(linked_list):
    fast_pointer = linked_list.head_node
    slow_pointer = linked_list.head_node
    while fast_pointer:
      fast_pointer = fast_pointer.get_next_node()
      if fast_pointer:
        fast_pointer = fast_pointer.get_next_node()
        slow_pointer = slow_pointer.get_next_node()

    print(f'Middle (right-weighted) is {slow_pointer.get_value()}')

ll = LinkedList(100)
ll.insert_beginning(200)
ll.insert_beginning(300)
ll.insert_beginning("Wombat1")
ll.insert_beginning("Wombat2")
ll.insert_beginning("Wombat3")
ll.insert_beginning("Wombat4")
ll.print()

ll.nth_last_node(1)
ll.nth_last_node(4)
ll.find_middle()
ll.remove_node(300)
ll.print()
ll.find_middle()
ll.remove_node("Wombat3")
ll.print()

ll.swap_nodes(100, 200)
ll.swap_nodes("Wombat2", "Wombat1")
ll.print()
ll.nth_last_node(2)
ll.find_middle()
