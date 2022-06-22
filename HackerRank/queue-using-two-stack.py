# -*- coding: utf-8 -*-
"""
Queue using Two Stacks
"""

class MyQueue(object):
    def __init__(self):
        self.first = []
    
    def peek(self):
        return self.first[0]
        
    def pop(self):
        self.first = self.first[1:]
        pass
        
    def put(self, value):
        self.first.append(value)
        pass
    
queue = MyQueue()
t = int(input())
for line in range(t):
    values = list(map(int, input().split()))
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print (queue.peek())