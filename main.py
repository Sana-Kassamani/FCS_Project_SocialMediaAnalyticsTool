from User import User

def main():
    user1=User("jack")
    user1.addGenre("Thriller")
    user1.addGenre("Comedy")
    user1.addGenre("Sci-Fi")
    user1.displayUser()
    user1.addBooksRead("Harry Potter and The Prisonor of Azkaban")
    user1.addBooksRead("Betrayed")
    user1.displayUser()
    user1.deleteBooksRead("betrayed")
    user1.addBooksCurrentlyReading("The Inner Circle")
    user1.addBooksToBeRead("How The Light Gets In")
    user1.displayUser()
    user1.changeName("Jacques")
    user1.displayUser()
    user2=User("Mary")
    user2.displayUser()
    user1.deleteGenre("sci-Fi")
    user1.displayUser()
    user1.deleteUser()
    user3=User("Ali")
    user3.displayUser()
    user4=User("ahmed")
    user4.displayUser()
    


main()
