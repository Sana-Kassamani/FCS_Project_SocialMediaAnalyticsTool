from User import User
from LinkedList import LinkedList
from Node import Node
from Network import Network
from Stack import Stack
from Heap import Heap
from Utilities import Utilities
from fillNetwork import fillNetwork
import json
def displayMainMenu():
    print("Menu:\n" +
            "\t1. Manage Users\n" +
            "\t2. Manage Network\n" + 
            "\t3. Exit Program\n")
def displayUserMenu():
    print("User Menu:\n" +
            "\t1. Create a new user\n" +
            "\t2. Delete an existing User\n" + 
            "\t3. Add a genre\n" +
            "\t4. Add Books Read\n" +
            "\t5. Add Books Currently Reading"+
            "\t6. Add Books To Be Read"+
            "\t7. Display User"+
            "\t8. Exit User")
    
def displayNetworkMenu():
    print("Network Menu:\n" +
            "\t1.  Add a vertex\n" +
            "\t2.  Add a connection\n" + 
            "\t3.  Delete Vertex\n" +
            "\t4.  Display Network\n" +
            "\t5.  Display nodes in Depth-First Search"+
            "\t6.  Display nodes in Breadth-First Search"+
            "\t7.  Find dhortest distance from vertex to all other vertices"+
            "\t8.  Check out connected components"+
            "\t9.  Recommend friends"+
            "\t10. Calculate average number of friends per user"+
            "\t11. Calculate graph density"+
            "\t12. Calculate local clustering coefficient for a certain user"+
            "\t13. Visulaize network"+
            "\t14. Exit Network")
def goToMain():
    displayMainMenu()
    option = input("Enter what do you wish to manage: ")
    while option != "3":
        if option == "1":
            goToUser()
        elif option == "2":
            goToNetwork()
        else:
            print("Invalid input.")
        displayMainMenu()
        option = input("Enter what do you wish to manage: ")

    print("Leaving program...")

def goToUser():
    User.showAllUsers()
    displayUserMenu()
    option = input("Enter what do you wish to do with users: ")
    while option != "8":
        if option == "1":
            name=input("Let's create a new user. Enter a name:")
            user=User(name)
        elif option == "2":
            id=input("Deleting user. Enter id of user you wish to delete:")
            user = User.selectUser(id)
            user.deleteUser()
        elif option == "3":
            id = input("Adding Genre. Enter id of user you wish to add genre to:")
            user = User.selectUser(id)
            genre= input("Enter genre you wish to add to ${user.name}:")
            user.addGenre(genre)
        elif option == "4":
            id = input("Adding to Books Read. Enter id of user you wish to add book to:")
            user = User.selectUser(id)
            book= input("Enter book you wish to add to Books Read of ${user.name}:")
            user.addBooksRead(book)
        elif option == "5":
            id = input("Adding to Books Currently Reading. Enter id of user you wish to add book to:")
            user = User.selectUser(id)
            book= input("Enter book you wish to add to Books Currently Reading of ${user.name}:")
            user.addBooksCurrentlyReading(book)
        elif option == "6":
            id = input("Adding to Books To Be Read. Enter id of user you wish to add book to:")
            user = User.selectUser(id)
            book= input("Enter book you wish to add to Books To Be Read of ${user.name}:")
            user.addBooksToBeRead(book)
        elif option == "7":
            id = input("Enter id of user you wish to display:")
            user = User.selectUser(id)
            user.displayUser()
        else:
            print("Invalid input.")
        User.showAllUsers()
        displayUserMenu()
        option = input("Enter what do you wish to do with users: ")

    print("Leaving User ...")
    goToMain()



        
        


            

def goToNetwork():
    pass

def main():
    net=fillNetwork()
    goToMain()
        
    




    # print("---------------User-------------------")
    # user1=User("jack")
    # user1.addGenre("Thriller")
    # user1.addGenre("Comedy")
    # user1.addGenre("Sci-Fi")
    # user1.displayUser()
    # user1.saveUserToJsonFile()
    # user1.addBooksRead("Harry Potter and The Prisonor of Azkaban")
    # user1.addBooksRead("Betrayed")
    # user1.displayUser()
    # user1.deleteBooksRead("betrayed")
    # user1.addBooksCurrentlyReading("The Inner Circle")
    # user1.addBooksToBeRead("How The Light Gets In")
    # user1.displayUser()
    # user1.changeName("Jacques")
    # user1.displayUser()
    # user2=User("Mary")
    # user2.displayUser()
    # user1.deleteGenre("sci-Fi")
    # user1.displayUser()
    # user1.deleteUser()
    # user3=User("Ali")
    # user3.displayUser()
    # user4=User("ahmed")
    # user4.displayUser()
    # print("------------------network-----------------")
    # user1=User("jack")
    # user2=User("Mary")
    # user3=User("Ali")
    # user1.addGenre("Drama")
    # user1.addGenre("Romance")
    # user1.addGenre("Fantasy")
    # user1.addGenre("Sci-Fi")
    # user2.addGenre("Thriller")
    # user2.addGenre("Drama")
    # user2.addGenre("Ya")
    # user2.addGenre("Crime")
    # user2.saveUserToJsonFile()
    # user3.addGenre("Romance")
    # user3.addGenre("Drama")
    # user3.addGenre("Ya")
    # user3.addGenre("Sci-fi")
    # user3.addGenre("Fantasy")
    # user4=User("Samah")
    # user5=User("Akram")
    # user4.addGenre("Romance")
    # user4.addGenre("Drama")
    # user5.addGenre("Thriller")
    # user5.addGenre("Crime")
    # user5.addGenre("Sci-Fi")
    # user6=User("ahmad")
    
    # net= Network()
    # net.addVertex(user1)
    # net.addVertex(user2)
    # net.addVertex(user3)
    # net.addVertex(user4)
    # net.addVertex(user5)
    # net.addVertex(user6)
    # net.displayNetwork()
    # net.addConnection(user1,user2)
    # net.addConnection(user2,user5)
    # net.displayNetwork()
    # net.addConnection(user2,user3)
    # net.addConnection(user3,user4)
    # net.addConnection(user1,user5)
    # net.addConnection(user2, user4)
    # net.displayNetwork()
    # dist= net.dijkstra(user4)

    # for i in dist:
    #     print("(",i.name,",", i.id,") :",dist[i])
    # net.addConnection(user1,user2)
    # net.addConnection(user2,user5)
    # net.addConnection(user2,user4)
    # net.addConnection(user1,user5)
    # net.addConnection(user3,user4)
    # net.addConnection(user3,user5)
    # net.addConnection(user3,user2)
    # net.addConnection(user3,user6)
    
    # net.displayNetwork()
    # recommend= net.recommendFriends(user1)
    # print("Recommended: ")
    # for r in recommend:
    #     print("(",r.name,",", r.id,")", end=" ")
    # print('\n')

    # print("average nb of friends / user:",net.calculateAverageNumberOfFriendsPerUser())

    # print ("density:",net.calculateGraphDensity())

    # print("clustering coefficient of ali:", net.calculateLocalClusteringCoefficient(user2))

    # net.dfs(user1)
    # print('\n')
    # net.bfs(user3)
    # components=net.connectedComponents()
    # print("there are",len(components)," components in network!")
    # for index,nodes in components.items():
    #     print(" ",index,":",end=" ")
    #     for user in nodes:
    #         print("(",user.name,",", user.id,")",end=" ")
    #     print('\n')
    # net=Network()
    # user0=User("0")
    # user1=User("1")
    # user2=User("2")
    # user3=User("3")
    # user4=User("4")
    # user5=User("5")
    # user6=User("6")
    # net.addVertex(user0)
    # net.addVertex(user1)
    # net.addVertex(user2)
    # net.addVertex(user3)
    # net.addVertex(user4)
    # net.addVertex(user5)
    # net.addVertex(user6)
    # net.addConnection(user0,user2,1/6)
    # net.addConnection(user0,user1,1/2)
    # net.addConnection(user2,user3,1/8)
    # net.addConnection(user1,user3,1/5)
    # net.addConnection(user3,user4,1/10)
    # net.addConnection(user3,user5,1/15)
    # net.addConnection(user4,user6,1/2)
    # net.addConnection(user5,user6,1/6)
    # net.displayNetwork()

    # dist= net.dijkstra(user0)
    # Utilities.mergeSort(dist,0,len(dist)-1,Utilities.compareWeights)
    # for i in dist:
    #    print("(",i.user.name,") :",i.weight)

    # def subtract(a,b):
    #     return a-b
    # list=[9,6,4,3,2,6,4,3,4,5,6,22,3,4,5,6,9]
    # print(list)
    # Utilities.mergeSort(list,0,len(list)-1,subtract)
    # print(list)
    
    # print()




    print("------------Heap-------------")
    # node1=Node(user1)
    # node1.setWeight(3)
    # node2=Node(user2)
    # node2.setWeight(7)
    # node3=Node(user3)
    # node3.setWeight(4)
    # node4=Node(User('Sam'))
    # node4.setWeight(6)
    # node5=Node(User('Samer'))
    # node5.setWeight(1)
    # node6=Node(User('alaa'))
    # node6.setWeight(11)
    # node7=Node(User('malek'))
    # node7.setWeight(22)
    # node8=Node(User('melhem'))
    # node8.setWeight(9)
    # node9=Node(User('manal'))
    # node9.setWeight(3)
    # node10=Node(User('salma'))
    # node10.setWeight(7)

    # h = Heap()
    # # h.enqueue(node1)
    # # h.displayNodes()
    # # h.enqueue(node2)
    # # h.displayNodes()
    # # h.enqueue(node3)
    # # h.displayNodes()
    # # h.enqueue(node4)
    # # h.displayNodes()
    # # h.enqueue(node5)
    # # h.displayNodes()
    # # h.enqueue(node6)
    # # h.displayNodes()
    # # h.enqueue(node7)
    # # h.displayNodes()
    # # h.enqueue(node8)
    # # h.displayNodes()
    # # h.enqueue(node9)
    # # h.displayNodes()
    # # h.enqueue(node10)
    # # h.displayNodes()
    # list=[]
    # list.append(0)
    # list.append(node1)
    # list.append(node2)
    # list.append(node3)
    # list.append(node4)
    # list.append(node5)
    # list.append(node6)
    # list.append(node7)
    # list.append(node8)
    # list.append(node9)
    # list.append(node10)
    # h.heapify(list)
    # h.displayNodes()
    # min= h.removeMin()
    # print("(",min.user.name,",", min.user.id,",",min.weight,")" )

    # h.displayNodes()
    print("-----------------linked list--------------")
    # l=LinkedList()
    # l.displayNodes()
    # l.addNodeToStart(user1)
    # l.displayNodes()
     
    # l.addNodeToStart(user2)
    # l.addNodeToStart(user3)
    # l.displayNodes()
    # l.removeNode(user2)
    # l.displayNodes()
    # l.removeNode(user1)
    # l.displayNodes()
    # l.removeNode(user3)
    # l.displayNodes()
    # stack = Stack()
    # stack.push(Node(user3))
    # stack.displayNodes()
    # stack.push(Node(user2))
    # print("top is :", stack.top())
    # stack.push(Node(user4))
    # stack.displayNodes()
    # stack.pop()
    # stack.displayNodes()
    # stack.pop()
    # stack.displayNodes()
    # stack.pop()
    # stack.displayNodes()
    # stack.pop()
    # stack.displayNodes()


main()
