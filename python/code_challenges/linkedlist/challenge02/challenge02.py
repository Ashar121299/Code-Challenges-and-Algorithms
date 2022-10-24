# Write here the code challenge solution

    
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        '''
        This fuction add a new node to the end of the
        linked list or add the first node
        if the linked list was already empty
        '''
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
    def middle_node (self):
        '''
        This function print linked list from middle
        node up to end 
        
        '''
        count=0
        nodes=[]
        current = self.head
        while current:
            count+=1
            current=current.next
            
        current = self.head
        for i in range (count//2):
            current=current.next
        
        while current is not None:
            nodes.append(current.value)
            current=current.next
        return nodes


        
if __name__=='__main__':   
    linkedList = LinkedList()
    node1 = Node(1)
    linkedList.append(node1)
    node2 = Node(2)
    linkedList.append(node2)
    node3 = Node(3)
    linkedList.append(node3)
    node4 = Node(4)
    linkedList.append(node4)
    node5 = Node(5)
    linkedList.append(node5)
    node6 = Node(6)
    linkedList.append(node6)
    print(linkedList.middle_node())



    
    
                
            