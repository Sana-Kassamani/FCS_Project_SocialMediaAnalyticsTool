# Network class definition:
# network is a graph data structure resembling the network of users in this social media platform
# As not all users may be connected to each other and edges are spaese, we will bw using an adjacency list to 
# represent this network

from User import User
from LinkedList import Node
from LinkedList import LinkedList

class Network:

    def __init__(self):
        self.vertices={}
    
    def addVertex(self, user):
        #O(V)
        if user in self.vertices:
            print("User already in network!")
            return
        self.vertices[user]=LinkedList()
        print("User (",user.name,",",user.id, ") added to network")

    def deleteVertex(self, user):
        #O(V)
        if user not in self.vertices:
            print("Cannot delete! User not in network!")
            return
        del self.vertices[user]
        print("User (",user.name,",",user.id, ") deleted from network")

    def calculateWeight(node1,node2):
        #O(N*M), N and M being numbers of genres for each user in node1 and node2 respectively
        weight =0
        for i in node1.user.genres:
            for j in node1.user.genres:
                if i == j :
                    weight +=1
        return weight

    def addConnection(self,user1, user2):
        #O(V)
        if user1 in self.vertices and user2 in self.vertices:
            node1=Node(user1)
            node2=Node(user2)
            weight=self.calculateWeight(node1,node2)
            node1.setWeight(weight)
            node2.setWeight(weight)
            self.vertices[user1].addNodeToStart(node2)
            self.vertices[user2].addNodeToStart(node1)


        elif user1 not in self.vertices and user2 not in self.vertices:
            print("Cannot Connect! Users not found in network.")
        else:
            print("Cannot Connect! One of users not found in netwrok.")

    def displayNetwork(self):
        #O(V*E), E is number of edges in network
        if not self.vertices:
            print("Network is empty!!")
            return
        print('\n')
        for user,friends in self.vertices.items():
            print("User (",user.name,",",user.id, ")", end=" ")
            friends.displayNodes()
        print('\n')
