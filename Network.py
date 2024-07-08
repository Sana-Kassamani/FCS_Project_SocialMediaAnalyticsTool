# Network class definition:
# network is a graph data structure resembling the network of users in this social media platform
# As not all users may be connected to each other and edges are spaese, we will bw using an adjacency list to 
# represent this network

from User import User
from Node import Node
from LinkedList import LinkedList
from Stack import Stack

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
        friend=self.vertices[user].head
        while friend:
            self.vertices[friend.user].deleteNode(user)
            friend= friend.next
        del self.vertices[user]
        print("User (",user.name,",",user.id, ") deleted from network")

    def calculateWeight(self,node1,node2):
        #O(N*M), N and M being numbers of genres for each user in node1 and node2 respectively
        weight = 0
        for i in node1.user.genres:
            for j in node2.user.genres:
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
            self.vertices[user1].addNodeToEnd(node2)
            self.vertices[user2].addNodeToEnd(node1)


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
            print("User (",user.name,",",user.id, ") :", end=" ")
            friends.displayNodes()
        print('\n')

    def dfs(self,root):
        if root not in self.vertices:
            print("Starting Node not in network")
            return
        st=Stack()
        visited = {}
        for vertex in self.vertices:
            visited[vertex.id]=False
        visited[root.id]=True
        print("visited is ", visited)
        st.push(Node(root))
        print("User (", root.name,",",root.id, ")", end=" ")
        while not st.isEmpty():
            # print("\n stack now is :")
            # st.displayNodes()
            # print('\n')
            # print("\n visited now is :")
            # print(visited)
            node= st.top()
            st.pop()
            curr = self.vertices[node.user].head
            # print("\n")
            # self.vertices[node.user].displayNodes()
            while curr :
                if not visited[curr.user.id]:
                    st.push(Node(curr.user))
                    print("User (", curr.user.name,",",curr.user.id, ")", end=" ")
                    visited[curr.user.id]=True
                # print("current is", curr.user.name,",",curr.next)
                curr = curr.next
               

