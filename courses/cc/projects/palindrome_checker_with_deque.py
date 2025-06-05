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
    if len(self.elements) > 0:
      return False
    return True
  def size(self):
    return len(self.elements)
  def peek_first(self):
    return self.elements[-1]
  def peek_last(self):
    return self.elements[0]
  def display_deque(self):
    print("Deque: ", ' | '.join(str(item) for item in self.elements))

def is_palindrome(candidate):
  deque = Deque()

  print("\nPalindrome candidate:", candidate)
  candidate = candidate.lower()
  candidate = candidate.replace(' ', '')
  candidate = candidate.replace(',', '')
  candidate = candidate.replace('.', '')
  candidate = candidate.replace('?', '')
  candidate = candidate.replace('!', '')
  candidate = candidate.replace('-', '')

   

  for char in candidate:
    deque.add_first(char)
  
  deque.display_deque()

  while deque.size() > 1:
    first = deque.remove_last()     
    last = deque.remove_first()
    if first != last:
      return False
  
  return True


if __name__ == '__main__':
  print("Is palindrome:", is_palindrome('Hello World'))
  print("Is palindrome:", is_palindrome('Level'))
  print("Is palindrome:", is_palindrome('Racecar'))
  print("Is palindrome:", is_palindrome('A Toyota'))
  print("Is palindrome:", is_palindrome('Step on no Pets'))
  print("Is palindrome:", is_palindrome('Do geese see God?'))
  print("Is palindrome:", is_palindrome('A man, a plan, a canal-Panama'))
  print("Is palindrome:", is_palindrome('Ah, Satan sees Natasha'))