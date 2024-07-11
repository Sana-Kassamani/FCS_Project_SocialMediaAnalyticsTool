# Queue class definition:
# Queue class will be used in implementing the Breadth-First Search (bfs) method of network class

from Node import Node

class Queue:

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self,node):
        #O(1)
        if self.size==0:
            self.head=node
            self.tail=node 
        else:
            self.tail.next = node
            self.tail = node
        self.size+=1

    def dequeue(self):
        #O(1)
        if self.size ==0:
            print("Cannot dequeue! Queue is empty!")
        elif self.size==1:
            curr = self.head
            self.head = None
            self.tail = None
            curr.next = None
            self.size -=1
        else:
            curr = self.head
            self.head = self.head.next
            curr.next = None
            self.size -=1
    
    def displayNodes(self):
        #O(N), N being number of node in Queue
        curr = self.head
        if not self.size:
            print("Queue is empty!!")
            return
        while curr:
            print("(",curr.user.name,",", curr.user.id,")" , end=" -> ")
            curr = curr.next
        print('\n')
        
