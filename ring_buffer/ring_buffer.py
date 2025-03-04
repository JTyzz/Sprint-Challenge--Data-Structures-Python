class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #code for buffer not full
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1

    #code for buffer full
    else:
      self.current = 0
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    return([i for i in self.storage if i is not None])