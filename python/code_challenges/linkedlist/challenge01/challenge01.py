# Write here the code challenge solution
def delete(node):
    '''
    This function take a  node as parameter ,and 
    deleted it by move pointer from previous node to 
    the next one
    '''
    temp = node.next
    node.value = temp.value
    node.next = temp.next
    temp.next=None



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

    def print_All(self):
        nodes=[]
        if self.head is None :
            print("empty linked list")
        else:
            current = self.head
            while current is not None:
                nodes.append(current.value)
                current = current.next
            return nodes
    
    

