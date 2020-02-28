from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
     

    def append(self, item):
      #if there's still capacity for storage, append new item to head
      if self.storage.length < self.capacity:
          self.storage.add_to_tail(item)
          self.current = self.storage.head
      #else, if the current is equal or more than the capacity
      else:
      # we need to overwrite the oldest node, remove from the head and add item to the tail
          overwritten_node = self.storage.head
          self.storage.remove_from_head()
          self.storage.add_to_tail(item)
          #if the overwritten node is the current node, move it to the tail
          if overwritten_node == self.current:
              self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # # TODO: Your code here
        list_buffer_contents.append(self.current.value)

        if self.current == self.storage.tail:
            node = self.storage.head
        else:
            node = self.current.next

        while node is not self.current:
            list_buffer_contents.append(node.value)
            node = node.next if node.next else self.storage.head

        return list_buffer_contents

        # return list_buffer_contents
        # list_buffer_contents = []

        # list_buffer_contents.append(self.current.value)

        # if self.current == self.storage.tail:
        #     node = self.storage.head
        # else:
        #     node = self.current.next

        # while node is not self.current:
        #     list_buffer_contents.append(node.value)
        #     node = node.next if node.next else self.storage.head

        # return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
