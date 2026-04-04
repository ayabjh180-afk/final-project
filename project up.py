##IY499 Practical Programming Assignment
##Example Project 2: Book Recommendation System#
# (Python Software Foundation, 2020)
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
                ["Abir", "The last day", "5"],
                ["Aya", "It ends with us", "4"],
                ["Diana", "The last day", "4"],
                ["Charlie", "Everyone but my self", "5"],
                ["Omar", "The culture map", "4"],
                ["Hibah", "The lord of the rings", "5"],
                ["sarah", "The ideal life", "4"],
                ["Tom", "Your heart", "3"],
                ["yehor", "It ends with us", "5"],
                ["Anka", "Anti fragile", "2"],
                ["sultan", "The culture map", "5"],
                ["Maggie", "The mointain is you", "5"],
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
            except ValueError 
                # and when the  rating is not a valid number  , the program should skip  the row 
                continue
            if The_user_name not in data: # checking if the name of the user exists in the dictionnary
            # the program should add the user in the dictionnary if he does not exist and set the rating of the book that he picked 
                data[The_user_name] = {}
            data[The_user_name][book_name] = rating

    except FileNotFoundError:
        print("File not found.Try again")

    return data
# the user will select a random book in the dataset
def select_random_books(data,num=5):
    books=[] # using an empty list to store the random books 
    for The_user_name in data: # loop through each user name
        for book_name in data[The_user_name]: # another loop to loop through each book has been picked by the user
            if book_name not in books:     # checks if the name of the book exists in the list
                books.append(book_name)    # if not selected, it should be added to the list
    #num=the number of book that the user can pick
    #i used min to make sure that teh user will not pick  more than the books that exists 
    num = min(num, len(books)) 
    select_random_books(random.sample(num)) # elect the random number of books from the list

    return  select_random_books()


# this function will ask the user to rate these books from 1 to 5
def collect_ratings(random_books):
    The_user_rating={} # this empty dictionnary to store teh user ratings 
    print("Rate these books from(1-5)")
    for book_name in  random_books:
        while True: # it keeps repeating until teh user enter a valid  rating
            rating=int(input("Enter your rating:"))
            if rating >=1 and rating<=5:            # to check that the rating is between 1 and 5 
                print("Thank you :)")
                The_user_rating [book_name]= rating
                break
            else:
                print(":( Try again.The number is invalid")
           
    return  The_user_rating
#This function compares the ratings of the new user with the existing users by checking common books
# calculates the difference between the users ratings.
def find_similar_users(data,The_user_rating):
    similarity={} # i create an empty dictionary to store the user name and  the similarity score
    for The_user_name in data:
        total=0   # to count the total difference
        books_count=0 # to calculate how many common books 
        for book_name in The_user_rating:  # to check the common books
            if book_name in data[The_user_name]:
                The_existinguser_rating=data[The_user_name][book_name]          #the rating of the existing user
                The_newuser_rating=The_user_rating[book_name]    # the rating of the new user
                # now the program will calculate the diference to see the similarity between two different users
                difference=abs(The_existinguser_rating-The_newuser_rating) # abs avoid negative numbers
                total+=difference # to add the difference
                books_count+=1
            
        if books_count>0:   # to check if  there is some common books
                The_avg = total / books_count              # this is to calculate the average difference of books
                similarity[The_user_name]=The_avg          # then store the results in the dictionary that i create earllier

    return similarity
#This function will suggest books to the user 

def books_recommendation(data,similarity,Thw_user_rating):
    recommended_books=[]
    for books in 








    return recommended_books








 