# Write your test here
import pytest
from challenge01 import *

def test_BDF():
    graph1 = Graph()

    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    e = graph1.add_node("E")
    f = graph1.add_node("F")

    graph1.add_edge( a,  b)
    graph1.add_edge( a,  c)
    graph1.add_edge( a,  e)
    graph1.add_edge( b,  d)
    graph1.add_edge( c,  f)
    graph1.add_edge( e,  d)
    graph1.add_edge( e,  f)
    
    

    traverse= graph1.BDF( a)

    arr=[]
    for value in traverse:
        arr.append(value.__str__())
    actual=arr

    extcepted = ["A", "B", "C", "E", "D", "F"]
    assert actual == extcepted