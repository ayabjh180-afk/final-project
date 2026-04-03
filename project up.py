#(Python Software Foundation, 2020)
import csv # to store and read data from the file 
#(Python, 2025)
import random # to pick random books so to not show the same book each time
#(matplotlib, 2024)
import  matplotlib.pyplot as plt # help to create graphs which helps the user to understand the data easily

books_data_file = "book_ratings.csv"


def create_file():
    try:
        # Check if file exists
       with open(books_data_file, "r"):
            pass
    except FileNotFoundError:
        with open(books_data_file, "w", newline="") as file:
        # to write data in a correct way into a csv file
            writer = csv.writer(file)

        rows=[  ["The_user_name", "book_name", "rating"],
                ["Abir", "To Kill a Mockingbird", "5"],
                ["Aya", "1984", "4"],
                ["Diana", "The Hunger Games", "4"],
                ["Charlie", "Brave New World", "5"],
                ["Omar", "Dune", "4"],
                ["Hibah", "1984", "5"],
                ["sarah", "Dune", "4"],
                ["Tom", "The Catcher in the Rye", "3"],
                ["yehor", "Brave New World", "5"],
                ["Anka", "1984", "2"],
                ["sultan", "Pride and Prejudice", "5"],
                ["Maggie", "Project Hail Mary", "5"],
            ]
        writer.writerows(rows) #to write multiple rows into the CSV file at once.
        

# we need a function to Opens the CSV file,Reads all rows, and converts them into a dictionary

def read_data():
    data = {} # using an empty dictionnary to store users, books, and ratings
# (www.w3schools.com, n.d.)
    try:
        with open (books_data_file, "r")  as file:
        #to read CSV files row by row as dictionaries to access each piece
            reader = csv.Reader(file)
            # to not read the first  header    row because it does not contain the real data
            next(reader)
            # here the program loop through  each row in the file  to get the user name and  the book he is looking for
            for row in reader:
                The_user_name = row[0]# the column [0] represents the user name
                book_name = row[1] # the column [1] represents the book name

            try:
                # I converted the rating when it is a  string  to a valid integer 
                rating = int(row[2])
            except ValueError:
                # and when the  rating is not a valid number  , the program should skip  the row 
                continue

            if The_user_name not in data: # checking if the name of the user exists in the dictionnary
            # the program should add the user in the dictionnary if he does not exist and set the rating of the book that he picked 
                data[The_user_name] = {}

            data[The_user_name][book_name] = rating

        

    except FileNotFoundError:
        print("File not found.Try again")

    return data


