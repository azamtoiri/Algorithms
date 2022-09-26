# LINKED LISTS

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def traversal(self):  # PRINT ALL NODE
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):   # INSERT A NEW HEADER
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):  # SEARCH ELEMENT
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def delete_node(self, data):  # NOT WORKS
        temp = self.head
        prev = temp
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def delete_tail(self):  # DELETE TAIL
        temp = self.head
        while temp.next.next is None:
            temp = temp.next
        temp.next = None


family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

print("Our Family")
family.traversal()

print("\nAdd Dave")
family.insert_new_header("Dave")
family.traversal()

print("\nSearch Bob ")
print(family.search("Bob"))

print("\nDelete Dave")
family.delete_node("Max")
family.traversal()

print("\nDelete Tail ")
family.delete_tail()
family.traversal()