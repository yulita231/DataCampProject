'''Steps to insert a node at the beginning:
1. Initialize a new node with the given data.
2. Set the 'next' pointer of the new node to the current head of the list.
3. Update the head of the list to point to the new node.
'''

def insert_at_beginning(self, data):
    # Create the new node
    new_node = self(data)
    # Check whether the linked list has a head node
    if self.head:
      # Point the next node of the new node to the head
      new_node.next = self.head
      self.head = new_node
    else:
      self.tail = new_node      
      self.head = new_node