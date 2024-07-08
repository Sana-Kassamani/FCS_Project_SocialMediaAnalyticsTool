# Node class definition:
# Node class will be used to represent the nodes of LinkedList, Stack, and Queue


class Node:
    def __init__(self,user):
        self.user=user
        self.next = None
        self.weight=0
    
    def setWeight(self,weight):
        #O(1)
        self.weight=weight