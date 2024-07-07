# None and LinkedList class definition:
# LinkedList class will be used to represent the graph aka network of this social media platform

from User import User

class Node:
    def __init__(self,user):
        self.user=user
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.size = 0
    
    def addNodeToStart(self, user):
        node = Node(user)
        if not self.size:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size +=1
        print("Added node",node.user.name,"to list")

    def removeNode(self, user):
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
        if not self.size:
            print("List is empty!!")
            return
        curr = self.head
        print('\n')
        while curr :
            print("(",curr.user.name,",", curr.user.id,")", end="->")
            curr = curr.next
        print('\n')