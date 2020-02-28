from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
     

    def append(self, item):
        # # if the current is up to  the capacity
        # if self.current == self.capacity:
          
        #     node = self.storage
        #     self.move_to_front(node)
        #     return node.value[0]

        # else:
        #   return None
        pass


      

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
