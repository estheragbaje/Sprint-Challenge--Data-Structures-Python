from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
     

    def append(self, item):
      #if there's still capacity for storage, append new item to head
      if self.storage.length < self.capacity:
          self.storage.add_to_head(item)
          self.current = item # the most recently appended item
      #if the current is up to the capacity
      if self.storage.length == self.capacity:
      # update current value to the new item
          self.current.value = item
      # if we're currently at the tail, and the most recent item is the head
      # we need to overwrite the oldest item
          if self.current is self.storage.tail:
          # go to head 
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = item
          else:
          # else, go to the next
            self.current = self.current.next
          
      

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_item = self.storage.tail
        # whilst item is not None, append the value to list
        while current_item is not None:
           list_buffer_contents.append(current_item.value)
           # Move current_item temporary variable onto next item
           current_item = current_item.prev

        # return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
