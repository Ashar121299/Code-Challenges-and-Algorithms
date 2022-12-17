class Node:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output

    def BDF(self, value):
        visited = []
        queue = [value]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                for edge in self.adj_list[node]:
                    queue.append(edge.vertex)
        return visited
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, value):
        node = Node(value)

        if not self.rear: 
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def pop(self):

        if self.front == None:
            return("This queue is empty")        
        if self.front == self.rear:
            self.rear = None
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

if __name__ == "__main__":

    graph1 = Graph()

    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)
    traverse = graph1.BDF(a)

    
    for value in traverse:
        print(value.__str__())
    




    