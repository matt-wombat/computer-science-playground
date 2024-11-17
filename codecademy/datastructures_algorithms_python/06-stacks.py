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

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding to stack: {}".format(value))
    else:
      print("Stack full. No room for: {}".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Watching: " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("Stack empty.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to watch left!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
movie_watchlist = Stack(5)
movie_watchlist.push("1. The Dark Knight Rises")
movie_watchlist.push("2. The Matrix")
movie_watchlist.push("3. The Equalizer")
movie_watchlist.push("4. Das Kartell")
movie_watchlist.push("5. Die Stunde der Patrioten")
movie_watchlist.push("6. Minority Report")
movie_watchlist.push("7. RED 2")

print("The first movie on your watchlist is: " + movie_watchlist.peek())
movie_watchlist.pop()
movie_watchlist.pop()
movie_watchlist.pop()
movie_watchlist.pop()
movie_watchlist.pop()
movie_watchlist.pop()
movie_watchlist.pop()