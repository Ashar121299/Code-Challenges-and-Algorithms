# Write here the code challenge solution
from inspect import stack


class Node:
    '''
    This class written to create a node represent the value 
    and pointer for both stack and queue
    '''
    def __init__(self,vlaue):
        '''
        this function written for assign value and
        pointer immeditly when create object
        '''
        self.next = None
        self.value = vlaue

class Stack:
    '''
    This class written to create a stack represent the all nodes
    and top pointer for stack will be created 
    '''

    def __init__(self):
        '''
        this function written for assign initial value of
        pointer and initial size of stack immeditly when create object
        '''
        self.top = None
        self.size = 0

    def push(self,value):
        '''
        This function written to push node inside stack and
        change the position of top pointer
        '''
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        '''
        This function written to pop node from stack and
        change the position of top pointer
        '''
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        '''
        this function written to return the position of top pointer
        '''
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        '''
        this function written to check if the stack is empty or not 
        and return bool vlaue
        '''
        if self.size == 0:
            return True 
        else:
            return False

    def get_size(self):
        '''this function return the size of stack
        '''
        return self.size
class Queue:
    '''
    This class written to create a queue by using two stack 
    '''
    def __init__(self):

        self.stack1=Stack()
        self.stack2=Stack()

    def push(self, value):
        '''
        This function written to push node inside first stack and
        change the position of top pointer
        '''
        self.stack1.push(value)

    def pop(self):
        '''
        This function written to pop node from seconed stack after push it from first one
        and change the position of top pointer
        '''
        while self.stack1.is_empty()== False:
            self.stack2.push(self.stack1.pop())
        while self.stack2.is_empty()== False:
            return self.stack2.pop()

    def peek(self):
        '''
        this function written to return the position of top pointer of seconed slack
        that represent the front pointer in queue
        '''
        while self.stack1.is_empty()== False:
            self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
    def empty(self):
        '''
        this function written to check if the queue is empty or not 
        and return bool vlaue by check the second stack
        '''
        return self.stack2.is_empty() 

if __name__=='__main__':
    queue1 = Queue()
    queue1.push(20)
    queue1.push(5)
    queue1.push(9)
    print(queue1.peek())
    print(queue1.pop())
    print(queue1.pop())
    print(queue1.empty())
    print(queue1.pop())
    print(queue1.empty())
    