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


class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")

      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add

      self.size += 1
    else:
      print("Sorry, no more room!")

  def dequeue(self):
    if self.is_empty() != True:
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")

      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = item_to_remove.get_next_node()

      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")

  def peek(self):
    if self.is_empty():
      print("Nothing to see here")
      return
    else:
      return self.head.get_value()

  def get_size(self):
    return self.size

  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()

  def is_empty(self):
    return self.get_size() == 0
