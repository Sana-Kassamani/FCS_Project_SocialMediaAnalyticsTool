# None and LinkedList class definition:
# LinkedList class will be used to represent the graph aka network of this social media platform

from User import User

class Node:
    def __init__(self,user):
        self.user=user
        self.next = None
        self.weight=0
    
    def setWeight(self,weight):
        #O(1)
        self.weight=weight

class LinkedList:
    def __init__(self):
        self.head=None
        self.size = 0
    
    def addNodeToStart(self, node):
        #O(1)
        if not self.size:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size +=1
        print("Added node",node.user.name,"to list")

    def removeNode(self, user):
        #O(N), N being number of nodes in list
        prev = None
        curr = self.head

        if not self.size:
            print("Cannot delete!List is empty.")
            return

        if curr.user.id == user.id:
            self.head= curr.next
            curr.next = None 
            self.size -=1
            print("Successfully deleted", user.name, "from list")
            return

        while curr and curr.user.id != user.id:
            prev = curr
            curr=curr.next
        if not curr:
            print("Cannot delete!",user.name, "not found in list!")
        else:
            prev.next = curr.next
            curr.next = None 
            self.size -= 1
            print("Successfully deleted", user.name, "from list")
        
    def displayNodes(self):
        #O(N), N being number of nodes in list
        if not self.size:
            print("List is empty!!")
            return
        curr = self.head
        
        while curr :
            print("(",curr.user.name,",", curr.user.id,")", end="->")
            curr = curr.next
        print('\n')