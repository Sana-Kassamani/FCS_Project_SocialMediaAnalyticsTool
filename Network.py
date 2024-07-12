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
from Utilities import Utilities
import math
import random
import networkx as nx
import matplotlib.pyplot as plt

class Network:

    def __init__(self):
        self.vertices={}
        self.edges=0
    
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

    #ToDo no duplicate connections
    def addConnection(self,user1, user2):
        #O(V)
        if user1 in self.vertices and user2 in self.vertices:
            if not self.isConnected(user1,user2):
                node1=Node(user1)
                node2=Node(user2)
                weight=self.calculateWeight(node1,node2)
                node1.setWeight(weight)
                node2.setWeight(weight)
                self.vertices[user1].addNodeToEnd(node2)
                self.vertices[user2].addNodeToEnd(node1)
                self.edges+=1
            else:
                print(user1.name, "and", user2.name," are already connected!")


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
        # print("User (", root.name,",",root.id, ")", end=" ")
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
                    # print("User (", curr.user.name,",",curr.user.id, ")", end=" ")
                    result.append(curr.user)
                    visited[curr.user.id]=True
                # print("current is", curr.user.name,",",curr.next)
                curr = curr.next
            # print('\n')
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
        dist=[]
        rootNode=Node(root)
        rootNode.setWeight(0)
        nodes=[]
        nodes.append(rootNode)
        for user in self.vertices:
            if user.id == root.id:
                continue
            node=Node(user)
            node.setWeight(math.inf)
            nodes.append(node)
        
        heap=Heap()
        heap.heapify(nodes)
        
        while not heap.isEmpty():
            minimum = heap.removeMin()
            dist.append(minimum)
            friend = self.vertices[minimum.user].head
            while friend:
                node, index = heap.includesUser(friend.user)
                if node:
                    if minimum.weight + (1/friend.weight) < node.weight:
                        heap.changeWeight( index,minimum.weight + (1/friend.weight))

                        
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
    
    def recommendFriends(self,user):
        recommended=[]
        dist=self.dijkstra(user)

        friends=[]
        friend=self.vertices[user].head
        while friend:
            friends.append(friend.user.id)
            friend=friend.next

        # print("friends:")
        # for i in friends:
        #     print("user ",i)

        # print()
        # for i in dist:
        #     print("user ",i.user.name,"id:",i.user.id,"  dist:",i.weight)

        # print()

        # for member in dist:
        #     if member.user.id in friends or member.user.id == user.id:
        #         dist.remove(member)
        # for i in dist:
        #     print("user ",i.user.name,"  dist:",i.weight)
        Utilities.mergeSort(dist,0,len(dist)-1,Utilities.compareWeights)
        i=0
        while i < len(dist) and len(recommended)== 0 :
            # make sure not to recommend the user himself or any user who is already a friend or first not connected user
            if dist[i].user.id != user.id and dist[i].user.id not in friends and dist[i] != math.inf:
                recommended.append(dist[i].user)
                return recommended
            i+=1
        
        # if all vertices in the user's component are his friends, then choose a random user from other components as recommendation
        not_connected=[]
        for node in dist:
            if node.weight == math.inf:
                not_connected.append(node.user)
        if not_connected:
            index= random.randint(0,len(not_connected)-1)
            recommended.append(not_connected[index])

        return recommended


    def calculateAverageNumberOfFriendsPerUser(self):
        total_sum=0

        for user,friends in self.vertices.items():
            sum_of_friends= friends.size
            total_sum+=sum_of_friends
        
        return round(total_sum / len(self.vertices),2)
    

    def calculateGraphDensity(self):
        nb_of_vertices = len(self.vertices)
        max_number_of_edges = (nb_of_vertices * (nb_of_vertices - 1)) / 2
        density=round(self.edges/max_number_of_edges,2)
        return density
    
    def isConnected(self,user1,user2):
        curr = self.vertices[user1].head
        while curr:
            if curr.user.id == user2.id:
                return True
            curr = curr.next
        return False

    def calculateLocalClusteringCoefficient(self,user):

        friends=[]
        curr = self.vertices[user].head
        while curr:
            friends.append(curr.user)
            curr=curr.next

        nb_of_triangles=0
        for user in friends:
            for user2 in friends:
                if self.isConnected(user,user2):
                    nb_of_triangles+=1

        #since it is an undirected graph
        nb_of_triangles = nb_of_triangles / 2

        degree=len(friends)
        local_clustering_coefficient= (2*nb_of_triangles)/(degree*(degree - 1))
        return round(local_clustering_coefficient,2)
    
    def visualizeNetwork(self):
        G = nx.Graph()
        for user, adj_list in self.vertices.items():
            G.add_node(user.name)
            current = adj_list.head
            while current:
                G.add_edge(user.name, current.user.name, weight=current.weight)
                current = current.next
        pos = nx.spring_layout(G)
        weights = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
        plt.show()
        



        

            
        


                
            
                

        




