from User import User
from LinkedList import LinkedList
from Node import Node
from Network import Network
from Heap import Heap
from Utilities import Utilities
from fillNetwork import fillNetwork

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
            "\t5. Add Books Currently Reading\n"+
            "\t6. Add Books To Be Read\n"+
            "\t7. Display User\n"+
            "\t8. Exit User\n")
    
def displayNetworkMenu():
    print("Network Menu:\n" +
            "\t1.  Add a vertex\n" +
            "\t2.  Add a connection\n" + 
            "\t3.  Delete Vertex\n" +
            "\t4.  Display Network\n" +
            "\t5.  Display nodes in Depth-First Search\n"+
            "\t6.  Display nodes in Breadth-First Search\n"+
            "\t7.  Find shortest distance from vertex to all other vertices\n"+
            "\t8.  Check out connected components\n"+
            "\t9.  Recommend friends\n"+
            "\t10. Calculate average number of friends per user\n"+
            "\t11. Calculate graph density\n"+
            "\t12. Calculate local clustering coefficient for a certain user\n"+
            "\t13. Exit Network\n")
    
def goToMain(net):
    displayMainMenu()
    option = input("Enter what do you wish to manage: ")
    while option != "3":
        if option == "1":
            goToUser(net )
        elif option == "2":
            goToNetwork(net)
        else:
            print("Invalid input.")
        displayMainMenu()
        option = input("Enter what do you wish to manage: ")

    print("Leaving program...")

def goToUser(net):
    User.showAllUsers()
    displayUserMenu()
    option = input("Enter what do you wish to do with users: ")
    while option != "8":
        if option == "1":
            name=input("Let's create a new user. Enter a name: ")
            user=User(name)


        elif option == "2":
            
            id=input("Deleting user. Enter id of user you wish to delete: ")
            while not id.isdigit():
                # make sure id can be parsed to int
                id=input("Id should be integer. Enter valid id: ")
            user = User.selectUser(int(id))
            while not user:
                # make sure user of id is present in platform
                id=input("Deleting user. Enter id of user you wish to delete: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))
            user.deleteUser()


        elif option == "3":
            id = input("Adding Genre. Enter id of user you wish to add genre to: ")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id: ")
            user = User.selectUser(int(id))
            while not user:
                id = input("Adding Genre. Enter id of user you wish to add genre to: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))
            genre= input("Enter genre you wish to add: ")
            user.addGenre(genre)


        elif option == "4":
            id = input("Adding to Books Read. Enter id of user you wish to add book to: ")
            while not id.isdigit():
                id = input("Id should be integer. Enter valid id: ")
            user = User.selectUser(int(id))
            while not user:
                id = input("Adding to Books Read. Enter id of user you wish to add book to: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))
            book= input("Enter book you wish to add to Books Read : ")
            user.addBooksRead(book)


        elif option == "5":
            id = input("Adding to Books Currently Reading. Enter id of user you wish to add book to: ")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id: ")
            user = User.selectUser(int(id))
            while not user:
                id = input("Adding to Books Currently Reading. Enter id of user you wish to add book to: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))
            book= input("Enter book you wish to add to Books Currently Reading: ")
            user.addBooksCurrentlyReading(book)


        elif option == "6":
            id = input("Adding to Books To Be Read. Enter id of user you wish to add book to: ")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id: ")
            user = User.selectUser(int(id))
            while not user:
                id = input("Adding to Books To Be Read. Enter id of user you wish to add book to: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))
            book= input("Enter book you wish to add to Books To Be Read: ")
            user.addBooksToBeRead(book)


        elif option == "7":
            id = input("Enter id of user you wish to display:")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id:")
            user = User.selectUser(int(id))
            while not user:
                id = input("Enter id of user you wish to display:")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id:")
                user = User.selectUser(int(id))
            user.displayUser()


        else:
            print("Invalid input.")

        print('\n')
        User.showAllUsers()
        displayUserMenu()
        option = input("Enter what do you wish to do with users: ")

    print("Leaving User ...")
    


def goToNetwork(net):
    net.printVertices()
    displayNetworkMenu()
    option = input("Enter what do you wish to do with network: ")
    while option != "13":
        if option == "1":
            # Either add vertex of an already present user or create a new user and add its vertex
            choice=input("Wanna create a new user or add existing one? Enter create OR add: ")
            while choice not in ["create","add"]:
                choice=input("Wanna create a new user or add existing one? Enter create OR add ONLY! ")
            if choice == "create":
                name=input("Let's create a new user. Enter a name: ")
                user=User(name)
                net.addVertex(user)
            else:
                User.showAllUsers()
                id=input("Let's create a new vertex. Enter a user id to put in vertex: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))
                while not user:
                    id=input("Deleting user. Enter id of user you wish to delete: ")
                    while not id.isdigit():
                        id=input("Id should be integer. Enter valid id: ")
                    user = User.selectUser(int(id))
                net.addVertex(user)



        elif option == "2":
            # get user 1
            id=input("Enter id of 1st user of connection: ")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id: ")
            user1 = User.selectUser(int(id))
            while not user1:
                id=input("Enter id of 1st user of connection: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user1 = User.selectUser(int(id))
            #get user 2
            id=input("Enter id of 2nd user of connection: ")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id: ")
            user2 = User.selectUser(int(id))
            while not user2:
                id=input("Enter id of 2nd user of connection: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user2 = User.selectUser(int(id))

            net.addConnection(user1,user2)


        elif option == "3":
            id=input("Deleting vertex. Enter id of user of vertex you wish to delete: ")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id: ")
            user = User.selectUser(int(id))
            while not user:
                id=input("Deleting vertex. Enter id of user of vertex you wish to delete: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))
            
            net.deleteVertex(user)


        elif option == "4":
            net.displayNetwork()


        elif option == "5":
            id=input("Enter id of user of vertex you wish to start dfs from: ")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id: ")
            user = User.selectUser(int(id))
            while not user:
                id=input("Enter id of user of vertex you wish to start dfs from: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))

            vertices=net.dfs(user)
            for vertex in vertices:
                print("User (", vertex.name,",",vertex.id, ")", end="  ")
            


        elif option == "6":
            id=input("Enter id of user of vertex you wish to start bfs from: ")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id: ")
            user = User.selectUser(int(id))
            while not user:
                id=input("Enter id of user of vertex you wish to start bfs from: ")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id: ")
                user = User.selectUser(int(id))
                
            vertices=net.bfs(user)
            for vertex in vertices:
                print("User (", vertex.name,",",vertex.id, ")", end="  ")


        elif option == "7":
            id = input("Enter id of user of vertex you wish to get shortest distance from:")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id:")
            user = User.selectUser(int(id))
            while not user:
                id = input("Enter id of user of vertex you wish to get shortest distance from:")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id:")
                user = User.selectUser(int(id))
            dist= net.dijkstra(user)
            Utilities.mergeSort(dist,0,len(dist)-1,Utilities.compareWeights)
            for i in dist:
                print("(",i.user.name,",",i.user.id,") :",i.weight)

        elif option == "8":
            components=net.connectedComponents()
            print("\nThere are",len(components),"components in network!\n")
            for index,nodes in components.items():
                print('\t',index,":",end=" ")
                for user in nodes:
                    print("(",user.name,",", user.id,")",end=" ")
                print('\n')
        
        elif option == "9":
            id = input("Enter id of user to recommend friends:")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id:")
            user = User.selectUser(int(id))
            while not user:
                id = input("Enter id of user to recommend friends:")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id:")
                user = User.selectUser(int(id))
            recommend=net.recommendFriends(user)
            if recommend:
                r=recommend[0]
                print("(",r.name,",", r.id,")")
        
        elif option == "10":
            print("Average nb of friends / user:",net.calculateAverageNumberOfFriendsPerUser())

        elif option == "11":
            print ("density:",net.calculateGraphDensity())

        elif option == "12":
            id = input("Enter id of user to calculate local clustering coefficient :")
            while not id.isdigit():
                id=input("Id should be integer. Enter valid id:")
            user = User.selectUser(int(id))
            while not user:
                id = input("Enter id of user to calculate local clustering coefficient :")
                while not id.isdigit():
                    id=input("Id should be integer. Enter valid id:")
                user = User.selectUser(int(id))
            print("Clustering coefficient of",user.name,"is :", net.calculateLocalClusteringCoefficient(user))

        else:
            print("Invalid input.")

        print('\n')
        net.printVertices()
        displayNetworkMenu()
        option = input("Enter what do you wish to do with network: ")

    print("Leaving Network ...")
    

def main():
    
    net=fillNetwork()
    goToMain(net)
    

main()
