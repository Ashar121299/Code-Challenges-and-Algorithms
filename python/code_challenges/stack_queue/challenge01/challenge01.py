# Write here the code challenge solution
from inspect import stack


class Node:
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        if self.size == 0:
            return True 
        else:
            return False

    def get_size(self):
        return self.size
class Queue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def push(self, value):
        self.stack1.push(value)

    def pop(self):
        while self.stack1.is_empty()== False:
            self.stack2.push(self.stack1.pop())
        while self.stack2.is_empty()== False:
            return self.stack2.pop()

    def peek(self):
        while self.stack1.is_empty()== False:
            self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
    def empty(self):
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
    