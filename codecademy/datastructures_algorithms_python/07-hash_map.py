class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  # Calculate hash
  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  # Compress hash into a number not greater than the size of the array
  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    # Hash index empty
    if current_array_value == None:
      self.array[array_index] = [key, value]
      return

    # Hash index containing the key already
    if key == current_array_value[0]:
      self.array[array_index] = [key, value]
      return

    # Warning: Collision! Hash index contains another key already
    # Open adressing scheme needed
    number_collisions = 1
    while current_array_value[0] != key:
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value == None:
        self.array[new_array_index] = [key, value]
        return   

      if current_array_value == key:
        self.array[new_array_index] = [key, value]
        return
      
      number_collisions += 1    

    # Hint: This implementation lacks application logic
    # for deleting keys

    return


  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value == None:
      return None
    
    if possible_return_value[0] == key:
      return possible_return_value[1]
    
    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return     

hash_map = HashMap(20)
hash_map.assign("256V", "Intel Core Ultra 7 256V, 4C+4c/8T, 2,4-4,8Ghz, 16GB LPDDR5X-8533, 12MB+14MB Cache")
hash_map.assign("258V", "Intel Core Ultra 7 258V, 4C+4c/8T, 2,4-4,8Ghz, 32GB LPDDR5X-8533, 12MB+14MB Cache")

print(hash_map.retrieve("258V"))
print(hash_map.retrieve("256V"))