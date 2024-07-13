# Function to save random users in json file and load at each run
# This func has been run once

import json
import random
from User import User

# load genres from json file
with open('genres.json') as genre_file:
  genres = json.load(genre_file)["Genres"]

# load books from json file
with open('books.json') as book_file:
  books = json.load(book_file)



def generateRandomUsers(num_users):
    # O(N), N being num of users
    users = []
    for i in range(num_users):
        name=input("Enter a name for user:")
        user = User(name)
        nb_of_genres=random.randint(1, 5)
        chosen_genres= random.sample(genres,nb_of_genres)
        for genre in chosen_genres:
           user.addGenre(genre)
        chosen_books=[]
        for i in range(9):
            book=random.choice(books[random.choice(chosen_genres)])
            while book in chosen_books:
               book=random.choice(books[random.choice(chosen_genres)])
            chosen_books.append(book)

        for book in chosen_books[:3]:
            user.addBooksRead(book)
        for book in chosen_books[3:6]:
           user.addBooksCurrentlyReading(book)
        for book in chosen_books[6:]:
            user.addBooksToBeRead(book)
        users.append(user.toDict())
    return users

# Generate 8 users 
users = generateRandomUsers(8) 


#save generated users to json
with open('users.json', 'w') as file:
    json.dump(users, file, indent=4)
