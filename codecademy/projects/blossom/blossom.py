# This program implements a Hash Map with a se


from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]
    
  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, val):
    array_index = self.compress(self.hash(key))
    payload = Node([key, val])
    lsit_at_index = self.array[array_index]

    for item in lsit_at_index:
      if item[0] == key:
        item[1] = val
        return
    
    lsit_at_index.insert(payload)

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    lsit_at_index = self.array[array_index]

    for item in lsit_at_index:
      if item[0] == key:
        return item[1]
    
    return None


blossom = HashMap(len(flower_definitions))

for elem in flower_definitions:
  blossom.assign(elem[0], elem[1])


print(blossom.retrieve('daisy'))
print(blossom.retrieve('rose'))



