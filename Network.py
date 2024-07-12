# Network class definition:
# network is a graph data structure resembling the network of users in this social media platform
# As not all users may be connected to each other and edges are spaese, we will bw using an adjacency list to 
# represent this network

from User import User
from Node import Node
from LinkedList import LinkedList
from Stack import Stack
from Queue import Queue
from Heap import Heap
import math

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
        weight = 1
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
        result=[]
        for vertex in self.vertices:
            visited[vertex.id]=False

        visited[root.id]=True
        st.push(Node(root))
        result.append(root)
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
                    result.append(curr.user)
                    visited[curr.user.id]=True
                # print("current is", curr.user.name,",",curr.next)
                curr = curr.next
            print('\n')
            return result
               
    def bfs(self, root):
        q=Queue()
        visited={}
        for vertex in self.vertices:
            visited[vertex.id]=False
        q.enqueue(Node(root))
        visited[root.id]=True
        print("User (", root.name,",",root.id, ")", end=" ")
        while not q.isEmpty():
            node = q.dequeue()
            curr = self.vertices[node.user].head
            while curr:
                if not visited[curr.user.id]:
                    q.enqueue(Node(curr.user))
                    visited[curr.user.id]=True
                    print("User (", curr.user.name,",",curr.user.id, ")", end=" ")
                curr=curr.next

    def dijkstra(self,root):
        dist={}
        rootNode=Node(root)
        rootNode.setWeight(0)
        nodes=[]
        nodes.append(rootNode)
        for user in self.vertices:
            if user.id== root.id:
                continue
            node=Node(user)
            node.setWeight(math.inf)
            nodes.append(node)
        
        heap=Heap()
        heap.heapify(nodes)
        heap.displayNodes()
        while not heap.isEmpty():
            minimum = heap.removeMin()
            dist[minimum.user]=minimum.weight 
            friend = self.vertices[minimum.user].head
            while friend:
                node, index = heap.includesUser(friend.user)
                if node:
                    if minimum.weight + (1/friend.weight) < node.weight:
                        heap.changeWeight( index,minimum.weight + (1/friend.weight))

                        print("changed somesing")
                friend=friend.next
        return dist
                
    def connectedComponents(self):
        components={}
        index=0
        visited=[]

        for user in self.vertices:
            if user not in visited:
                nodes=self.dfs(user)
                components[index]=nodes
                index+=1
                visited+=nodes
        
        return components
            
                

        




