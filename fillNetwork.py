# Function to generate random connections between loaded random users from json file
# This func runs once at each run of main

import json
import random
from User import User
from Network import Network



def fillNetwork():
#O(N*N), N being number of users
    net = Network()
    with open('users.json') as users_file:
        users = json.load(users_file)

    #create user object for each user in json file and add to network as vertex
    for user in users:
        new_user=User.fromDict(user)
        net.addVertex(new_user)
    
    # Arbitrary number of connections
    num_connections = len(users)   
    for _ in range(num_connections):
        # connection between 2 random users
        user1, user2 = random.sample(list(net.vertices.keys()), 2)
        net.addConnection(user1, user2) # O(V)
        
    return net


