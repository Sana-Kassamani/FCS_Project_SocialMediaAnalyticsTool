
from Node import Node

class Stack:

    def __init__(self):
        self.head=None
        self.size=0
    
    def push(self,node):
        #O(1)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        #O(1)
        if self.size == 0:
            print("No node to pop! Stack is empty!")
            return
        top = self.head
        self.head= top.next
        top.next = None
        self.size-=1

    def top(self):
        if self.size ==0:
            print("No node at top! Stack is empty!")
            return
        return self.head
    
    def isEmpty(self):
        return self.size ==0
    
    def displayNodes(self):
        #O(N), N being number of nodes in list
        if not self.size:
            print("Stack is empty!!")
            return
        curr = self.head
        
        while curr :
            print("(",curr.user.name,",", curr.user.id,")" , end=" -> ")
            curr = curr.next
        print('\n')