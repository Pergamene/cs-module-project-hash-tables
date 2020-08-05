class HashTableEntry:
  """
  Linked List hash table key/value pair
  """
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

  def get_key(self):
    return self.key
  
  def get_value(self):
    return self.value

  def set_value(self, value):
    self.value = value

  def get_next(self):
    return self.next

  def set_next(self, entry):
    self.next = entry

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
  """
  A hash table that with `capacity` buckets
  that accepts string keys
  Implement this.
  """
  def __init__(self, capacity=MIN_CAPACITY):
    # Your code here
    self.table = [None] * capacity
    self.capacity = capacity  
    self.length = 0

  def __len__(self):
    return self.length

  def get_num_slots(self):
    """
    Return the length of the list you're using to hold the hash
    table data. (Not the number of items stored in the hash table,
    but the number of slots in the main list.)
    One of the tests relies on this.
    Implement this.
    """
    # Your code here
    return self.capacity

  def get_load_factor(self):
    """
    Return the load factor for this hash table.
    Implement this.
    """
    # Your code here
    return self.length / self.capacity

  def check_resize(self):
    load_factor = self.get_load_factor()
    if load_factor > 0.7:
      self.resize(self.capacity * 2)
    if load_factor < 0.2:
      if self.capacity == MIN_CAPACITY:
        return
      half = int(self.capacity / 2)
      if half > MIN_CAPACITY:
        self.resize(half)
      else:
        self.resize(MIN_CAPACITY)

  def fnv1(self, key):
    """
    FNV-1 Hash, 64-bit
    Implement this, and/or DJB2.
    """
    # Your code here
    hash_val = 14695981039346656037
    bytes_arr = key.encode('utf-8')
    for byte in bytes_arr:
      hash_val *= 1099511628211
      hash_val ^= byte
    return hash_val

  def hash_index(self, key):
    """
    Take an arbitrary key and return a valid integer index
    between within the storage capacity of the hash table.
    """
    return self.fnv1(key) % self.capacity

  def _add_to_list(self, node, key, value):
    entry = node
    if entry.get_key() == key:
        entry.set_value(value)
        return
    while entry.get_next() is not None:
      entry = entry.get_next()
      if entry.get_key() == key:
        entry.set_value(value)
        return
    entry.set_next(HashTableEntry(key, value))
    self.length += 1

  def _add_to_table(self, table, key, value):
    key_hash_index = self.hash_index(key)
    entry = table[key_hash_index]
    if entry is None:
      table[key_hash_index] = HashTableEntry(key, value)
      self.length += 1
    else:
      self._add_to_list(entry, key, value)

  def put(self, key, value):
    """
    Store the value with the given key.
    Hash collisions should be handled with Linked List Chaining.
    Implement this.
    """
    # Your code here
    self._add_to_table(self.table, key, value)
    self.check_resize()

  def delete(self, key):
    """
    Remove the value stored with the given key.
    Print a warning if the key is not found.
    Implement this.
    """
    # Your code here
    key_hash_index = self.hash_index(key)
    entry = self.table[key_hash_index]
    if entry is not None:
      if entry.get_key() == key:
        self.table[key_hash_index] = entry.get_next()
      else:
        while entry.get_next() is not None:
          if entry.get_next().get_key() == key:
            entry.set_next(entry.get_next().get_next())
            self.length -= 1
            self.check_resize()
            return
          else:
            entry = entry.get_next()
    print(f'The table does not contain the key: {key}')

  def get(self, key):
    """
    Retrieve the value stored with the given key.
    Returns None if the key is not found.
    Implement this.
    """
    # Your code here
    key_hash_index = self.hash_index(key)
    entry = self.table[key_hash_index]
    if entry is None:
      return None
    if entry.get_key() == key:
      return entry.get_value()
    while entry.get_next() is not None:
      entry = entry.get_next()
      if entry.get_key() == key:
        return entry.get_value()
    return None

  def resize(self, new_capacity):
    """
    Changes the capacity of the hash table and
    rehashes all key/value pairs.
    Implement this.
    """
    # Your code here
    new_table = [None] * new_capacity
    self.capacity = new_capacity
    for i in range(len(self.table)):
      entry = self.table[i]
      if entry is not None:
        self._add_to_table(new_table, entry.get_key(), entry.get_value())
        while entry.get_next() is not None:
          entry = entry.get_next()
          self._add_to_table(new_table, entry.get_key(), entry.get_value())
    self.table = new_table

if __name__ == "__main__":
  ht = HashTable(8)

  ht.put("line_1", "'Twas brillig, and the slithy toves")
  ht.put("line_2", "Did gyre and gimble in the wabe:")
  ht.put("line_3", "All mimsy were the borogoves,")
  ht.put("line_4", "And the mome raths outgrabe.")
  ht.put("line_5", '"Beware the Jabberwock, my son!')
  ht.put("line_6", "The jaws that bite, the claws that catch!")
  ht.put("line_7", "Beware the Jubjub bird, and shun")
  ht.put("line_8", 'The frumious Bandersnatch!"')
  ht.put("line_9", "He took his vorpal sword in hand;")
  ht.put("line_10", "Long time the manxome foe he sought--")
  ht.put("line_11", "So rested he by the Tumtum tree")
  ht.put("line_12", "And stood awhile in thought.")

  print("")

  # Test storing beyond capacity
  for i in range(1, 13):
    print(ht.get(f"line_{i}"))

  # Test resizing
  old_capacity = ht.get_num_slots()
  ht.resize(ht.capacity * 2)
  new_capacity = ht.get_num_slots()

  print(f"\nResized from {old_capacity} to {new_capacity}.\n")

  # Test if data intact after resizing
  for i in range(1, 13):
    print(ht.get(f"line_{i}"))

  print("")
