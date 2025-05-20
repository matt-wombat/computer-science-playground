class Deque:
  def __init__(self):
    self.elements = []
  def add_first(self, item):
    self.elements.append(item)
  def add_last(self, item):
    self.elements.insert(0, item)
  def remove_first(self):
    item = self.elements.pop()
    return item
  def remove_last(self):
    item = self.elements.pop(0)
    return item
  def is_empty(self):
    return len(self.elements) == 0
    
  def size(self):
    return len(self.elements)

  def peek_first(self):
    return self.elements[-1]
  def peek_last(self):
    return self.elements[0]
  def display_deque(self):
    print("Deque content:", ' | '.join(str(item) for item in self.elements))

if __name__ == '__main__':
  deque = Deque()
  deque.add_first(1974)
  deque.add_first(1990)
  deque.add_last(1954)
  deque.add_first(2014)
  deque.display_deque()

  print("Popped first value: " + str(deque.remove_first()))
  print("Popped last value: " + str(deque.remove_last()))
  print("Is empty:", deque.is_empty())
  print("Size:", deque.size())

  print("Popped first value: " + str(deque.remove_first()))
  print("Is empty:", deque.is_empty())
  print("Size:", deque.size())

  deque.display_deque()