# Write your test here
import pytest
from challenge02 import *
def test_case1():
    s1="[]()"
    stack1=Stack()
    actual=stack1.parentheses(s1)
    expected=True
    assert actual == expected

def test_case2():
    s2="[({)])"
    stack2=Stack()
    actual=stack2.parentheses(s2)
    expected=False
    assert actual == expected 

def test_case3():
    s2="([])"
    stack2=Stack()
    actual=stack2.parentheses(s2)
    expected=True
    assert actual == expected 

def test_case4():
    s2="(}[)[}"
    stack2=Stack()
    actual=stack2.parentheses(s2)
    expected=False
    assert actual == expected 

