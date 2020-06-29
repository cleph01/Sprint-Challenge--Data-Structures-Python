import time

### START Linked List

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None # Stores a node, that corresponds to our first node in the list 
        self.tail = None # stores a node that is the end of the list
  
    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value 

    def contains(self, value):
        if self.head is None:
            return False
        
        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head
    
        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True
    
            # otherwise, go to the next node
            current_node = current_node.next_node
        return False 
  
    def get_max(self):

        # Variable to hold current max
        curr_max = None

        current_node = self.head
        
        while current_node is not None:
           
            # check if current_node value is > then curr_max
            if curr_max is None or current_node.value > curr_max:
                
                curr_max = current_node.value

            current_node = current_node.next_node

        return curr_max

### END Linked List


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

linked_list = LinkedList()


# Replace the nested for loops below with your improvements
# for name_1 in names_1:

#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

for name_1 in names_1:

    linked_list.add_to_tail(name_1)

for name_2 in names_2:

    if linked_list.contains(name_2):

        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
