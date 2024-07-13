#User class definition:
# User has :
#   - unique id
#   - Name
#   - Favorite Genres
#   - Shelves containg books they read, currently reading or to be read

import json

class User:
    #user static instance variables
    next_id=1
    valid_ids=[]
    users=[]

    def __init__(self,name):
        # makes sure each user has unique id and ids are reused after deletion
        # if there are any valid ids from deleted users, use them
        if User.valid_ids :
            self.id=User.valid_ids[0]
            User.valid_ids.pop(0)
        else:
        # else use the next valid id
            self.id=User.next_id
            User.next_id+=1

        self.name=name

        self.genres=[]

        self.shelves=dict(
        {
            "Read":[],
            "Currently Reading":[],
            "To Be Read":[]
        })
        User.users.append(self)
        print("New User", name , "added!")

    @staticmethod
    def showAllUsers():
        print("Users in platform are:")
        print("---------------------------------------------------------")
        count = 0
        for user in User.users:
            count +=1
            print("[Id:",user.id," Name:",user.name,"]", end="   ")
            if count % 3 == 0:
                print('\n')
            print('\n')
        print("---------------------------------------------------------")
        print('\n')
            

    @staticmethod
    def selectUser(id):
        for user in User.users:
            if user.id == id:
                return user
        print("No user with id",id)

    def changeName(self,name):
        #O(1)
        self.name=name
        print("Name changed to",name)
    
    def getName(self):
        #O(1)
        return self.name
    
    def addGenre(self,genre):
        #O(N), N being number of genres
        if genre.capitalize() not in self.genres:
            self.genres.append(genre.capitalize())
            print("Added genre :",genre)
        else:
            print(genre,"already in Favorite Genres of",self.name)

    def deleteGenre(self,genre):
        #O(N), N being number of genres
        if genre.capitalize() not in self.genres:
            print("Cannot delete!",genre,"not in Favorite Genres of",self.name)
            return
        self.genres.remove(genre.capitalize())
        print(genre, "successfully removed from genres!")

    def getGenres(self):
        #O(1)
        return self.genres
    
    def addBookToShelve(self,book,key):
        #O(N), n being nb of books in shelves[key]
        if book in self.shelves[key]:
            print(book, "already in book shelf", key)
            return
        self.shelves[key].append(book)
        print(book,"added to shelf",key)
    
    def addBooksRead(self,book):
        #O(N), n being nb of books in shelves["Read"]
        self.addBookToShelve(book,"Read")
    
    def addBooksCurrentlyReading(self,book):
        #O(N), n being nb of books in shelves["Currently Reading"]
        self.addBookToShelve(book,"Currently Reading")

    def addBooksToBeRead(self,book):
        #O(N), n being nb of books in shelves["To Be Read"]
        self.addBookToShelve(book,"To Be Read")
    
    def deleteBooksFromShelve(self,book,key):
        #O(N), n being nb of books in shelves[key]
        if book not in self.shelves[key]:
            print("Cannot delete!",book, "not in book shelf", key)
            return
        self.shelves[key].remove(book)
        print(book,"deleted from shelf",key)

    def deleteBooksRead(self,book):
        #O(N), n being nb of books in shelves["Read"]
        self.deleteBooksFromShelve(book,"Read")
    
    def deleteBooksCurrentlyReading(self,book):
        #O(N), n being nb of books in shelves["Currently Reading"]
        self.deleteBooksFromShelve(book,"Currently Reading")

    def deleteBooksToBeRead(self,book):
        #O(N), n being nb of books in shelves["To Be Read"]
        self.deleteBooksFromShelve(book,"To Be Read")

    def getBooksRead(self):
        return self.shelves["Read"]
    
    def getBooksCurrentlyReading(self):
        return self.shelves["Currently Reading"]
    
    def getBooksToBeRead(self):
        return self.shelves["To Be Read"]
    
    def displayUser(self):
        user=""
        user+= "\tID : " + str(self.id) + "\n"
        user+= "\tName : "+ self.name + "\n"
        user+= "\tFavorite Genres : " 
        user+=(", ").join(self.genres)
        user += "\n"
        user+= "\tShelves : \n" 
        for shelf,books in self.shelves.items():
            user += "\t\t" + shelf +": \n\t\t\t"
            user+= (", ").join(books)
            user+= "\n"
        print("\n",user)
    
    def deleteUser(self):
        User.valid_ids.append(self.id)
        User.users.remove(self)
        name=self.name
        self.id=None
        self.name=""
        self.genres=[]
        self.shelves={}
        print("Deleted user",name)

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'genres': self.genres,
            'shelves': self.shelves
        }
    
    @staticmethod
    def fromDict(data):
        user = User(data['name'])
        user.id = data['id']
        user.genres = data['genres']
        user.shelves = data['shelves']
        return user
    