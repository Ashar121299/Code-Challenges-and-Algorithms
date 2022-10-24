# Write your test here
from challenge01 import delete


def test_case1():
    class Node:
        def __init__(self,value):
           self.value = value
           self.next = None
    class LinkedList:
        def __init__(self):
          self.head = None

        def append(self, node):
            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
    
    linkedList = LinkedList()
    node1 = Node(9)
    linkedList.append(node1)
    node2 = Node(1)
    linkedList.append(node2)
    node3 = Node(5)
    linkedList.append(node3)
    node4 = Node(8)
    linkedList.append(node4)
    assert delete(linkedList,node3)==[9, 1, 8]



def test_case2():
    class Node:
        def __init__(self,value):
           self.value = value
           self.next = None
    class LinkedList:
        def __init__(self):
          self.head = None

        def append(self, node):
            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
    
    linkedList = LinkedList()
    node1 = Node(4)
    linkedList.append(node1)
    node2 = Node(5)
    linkedList.append(node2)
    node3 = Node(9)
    linkedList.append(node3)
    node4 = Node(7)
    linkedList.append(node4)
    assert delete(linkedList,node3)==[4, 5, 7]


def test_case3():
    class Node:
        def __init__(self,value):
           self.value = value
           self.next = None
    class LinkedList:
        def __init__(self):
          self.head = None

        def append(self, node):
            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
    
    linkedList = LinkedList()
    node1 = Node(1)
    linkedList.append(node1)
    node2 = Node(3)
    linkedList.append(node2)
    node3 = Node(7)
    linkedList.append(node3)
    node4 = Node(9)
    linkedList.append(node4)
    assert delete(linkedList,node2)==[1, 7, 9]


def test_case4():
    class Node:
        def __init__(self,value):
           self.value = value
           self.next = None
    class LinkedList:
        def __init__(self):
          self.head = None

        def append(self, node):
            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
    
    linkedList = LinkedList()
    node1 = Node(15)
    linkedList.append(node1)
    node2 = Node(26)
    linkedList.append(node2)
    node3 = Node(8)
    linkedList.append(node3)
    node4 = Node(10)
    linkedList.append(node4)
    assert delete(linkedList,node2)==[15, 8, 10]










