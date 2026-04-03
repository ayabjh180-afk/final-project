# ============================================
# #########   BOOK PROGRAM  #################
# ============================================
import csv        # to read/write CSV files

FILE_NAME = "books.csv"
# ==========================================
# FUNCTION: Create File
# This function creates a new CSV file and writes
# a few example books and ratings into it.
# ========================================

print("hello")

def create_starter_books():
    # open a new file to write data
    file = open(FILE_NAME, "w")
    print("Creating your book file...")

    file.write("user,book,rating\n")
    # write some example data :users and their book ratings
    file.write("Lily,Harry Potter,5\n")
    file.write("Emma,The Hobbit,4\n")
    file.write("Sophie,The Great Gatsby,5\n")
    file.write("Noah,1984,4\n")
    file.write("Olivia,The Catcher in the Rye,3\n")
    print(" Added some example book ratings!")
    file.close()
    print("File is ready to use!")
    print("hello word ")
# ============================================
########### dictionary dataset ##########
# ============================================
book_ratings = {
    "Lily": {"Harry Potter": 5, "Little Women": 4, "Matilda": 5},
    "Emma": {"The Hobbit": 4, "Pride and Prejudice": 5, "Anne of Green Gables": 4},
    "Sophie": {"The Great Gatsby": 5, "To Kill a Mockingbird": 4},
    "Noah": {"1984": 4, "The Catcher in the Rye": 3},
    "Olivia": {"The Hunger Games": 5, "Twilight": 4}
}

# ============================================
# FUNCTION: Show All Books
# Displays all books in the dataset.
# ============================================


def show_books(book_ratings):
    print("List of all books:")  
# Loop through each person in the dictionary
    for person in book_ratings:
        # Loop through each book that person has
        for book in book_ratings[person]:
           rating = book_ratings[person][book]
           print(person, "gave", book, "a rating of", rating, "stars")

#============================================
# FUNCTION: Search for a book
# ============================================
def search_book(book_ratings):
    name = input("Enter book name to search: ")

    for person in book_ratings:
        for book in book_ratings[person]:
            if name in book:
                print(person, "rated", book)
# ============================================
# ######### MAIN PROGRAM  ###################
# ============================================

print("Welcome to my Book Program")

show_books(book_ratings)
search_book(book_ratings)