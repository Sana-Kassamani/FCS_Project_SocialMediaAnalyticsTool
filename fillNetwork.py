import json
import random
from User import User
from Network import Network


# Assuming User and Network classes are already defined
def fillNetwork():

    net = Network()
    with open('users.json') as users_file:
        users = json.load(users_file)

    for user in users:
        new_user=User.fromDict(user)
        net.addVertex(new_user)
    
    num_connections = len(users) * 2  # Arbitrary number of connections
    for _ in range(num_connections):
        user1, user2 = random.sample(list(net.vertices.keys()), 2)
        net.addConnection(user1, user2)
    return net

net=fillNetwork()

net.displayNetwork()
