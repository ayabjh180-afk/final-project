##IY499 Practical Programming Assignment
##Example Project 2: Book Recommendation System
# (Python Software Foundation, 2020)
import csv # to store and read data from the file 
#(Python, 2025)
import random # to pick random books so to not show the same book each time
#(matplotlib, 2024)
import  matplotlib.pyplot as plt # help to create graphs which helps the user to understand the data easily

books_data_file = "book_ratings.csv"

#(Python, n.d.)
#(Python, 2024)

def create_file():
    try:
        # Check if file exists
       with open(books_data_file, "r",encoding="utf-8") as file :
            pass
    except FileNotFoundError:
       
        with open(books_data_file, "w", newline="",encoding="utf-8") as file:
        # to write data in a correct way into a csv file
            writer = csv.writer(file)

            rows=[  ["The_user_name", "book_name", "rating"],
                    ["Abir", "The last day", "5"],
                    ["Abir", "The culture map", "2"],
                    ["Aya", "It ends with us", "4"],
                    ["Aya", "Your heart", "4"],
                    ["Diana", "The last day", "4"],
                    ["Charlie", "Everyone but my self", "5"],
                    ["Omar", "The culture map", "4"],
                    ["Hibah", "The lord of the rings", "1"],
                    ["Hibah", "The mountain is you", "3"],
                    ["sarah", "The ideal life", "4"],
                    ["Tom", "Your heart", "3"],
                    ["justin", "It ends with us", "5"],
                    ["Anka", "Anti fragile", "2"],
                    ["sultan", "The culture map", "3"],
                    ["sultan", "The ideal life", "2"],
                    ["Maggie", "The mountain is you", "5"],
                    ["Maggie", "Anti fragile", "3"],
                    ["Maggie", "The last day", "4"],
                 ]
            writer.writerows(rows) #to write multiple rows into the CSV file at once.
        print("CSV file created successfully!")

# we need a function to Opens the CSV file,Reads all rows, and converts them into a dictionary

def read_data():
    data = {} # using an empty dictionnary to store users, books, and ratings
# (www.w3schools.com, n.d.)
# (Google.com, 2023)
    try:
        with open (books_data_file, "r", encoding="utf-8")  as file:
        #to read CSV files row by row as dictionaries to access each piece
        ## DictReader uses the first row as keys for a dictionary
            reader = csv.DictReader(file)
            # to not read the first  header    row because it does not contain the real data
            # here the program loop through  each row in the file  to get the user name and  the book he is looking for
            for row in reader:
                if not row["The_user_name"] or not row["book_name"]:
                    continue
                The_user_name = row["The_user_name"]
                book_name = row["book_name"] 
                try:
                # I converted the rating when it is a  string  to a valid integer 
                    rating = int(row["rating"])
                    if The_user_name not in data:  # checking if the name of the user exists in the dictionnary
                        data[The_user_name]={}   # the program should add the user in the dictionnary if he does not exist and set the rating of the book that he picked
                        data[The_user_name][book_name] = rating
                except ValueError :
                # and when the  rating is not a valid number  , the program should skip  the row 
                    continue
          
    except FileNotFoundError:
        print("Error: The data file was not found.")   

    return data
# the user will select a random book in the dataset
def select_random_books(data,num=5):
    all_books=set() ## Using a set automatically prevents duplicate book names
    for The_user_name in data: # loop through each user name
        for book_name in data[The_user_name]: # another loop to loop through each book has been picked by the user
            all_books.add(book_name)    # if not selected, it should be added to the list
    #convert to a list only at the end so random.sample can read it
    books_list=list(all_books)
    if not  books_list:
        return []
    #I used min to make sure that teh user will not pick  more than the books that exists 
    num = min(num, len(books_list))  ##num=the number of book that the user can pick
    random_books=random.sample(books_list,num) # select the random number of books from the list

    return  random_books


# this function will ask the user to rate these books from 1 to 5
def collect_ratings(random_books):
    The_user_rating={} # this empty dictionnary to store teh user ratings 
    
    for book_name in  random_books:
        while True: # it keeps repeating until teh user enter a valid  rating
            try:
                rating=int(input(f"Enter your rating for this book:'{book_name}'(1-5): ")) # show the book name so the user can rate it 
                
                if  1<=rating<=5:            # to check that the rating is between 1 and 5 
                    print("Thank you :)")
                    The_user_rating [book_name]= rating
                    break   #to move to the next book 
                else:
                    print(":( Try again.The number must be between 1 and 5.")

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5")
            
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
                The_user_in_data=data[The_user_name][book_name]          #the rating of the existing user
                The_new_user_rating=The_user_rating[book_name]    # the rating of the new user
                # now the program will calculate the diference to see the similarity between two different users
                difference=abs(The_user_in_data-The_new_user_rating) # abs avoid negative numbers
                total+=difference # to add the difference
                books_count+=1
            
        if books_count>0:   # to check if  there is some common books
                The_avg = total / books_count              # this is to calculate the average difference of books
                similarity[The_user_name]=The_avg          # then store the results in the dictionary that i create earllier

    return similarity
#This function will suggest books to the user 
# (Python documentation, n.d.)
#(Python, n.d.)
def books_recommendation(data,similarity,The_user_rating):
    recommended_books={}                   # this dictionary to store the recommended books

    for The_user_name in similarity:  # to check the common books
            if similarity [The_user_name]<=2.5: # TO PICK similar users
                for book_name in  data[The_user_name]:    # loop through all the books that exist in the data
                    if book_name not in The_user_rating:
                        # We store the book's rating to help us sort later
                        # (This takes the rating from the person in our data)

                        rating_value = data[The_user_name][book_name]
                        #Check if we already found this book from another similar person
                        #If it's new, or if this person liked it more, update the  recommendations
                        # If we find the same book from multiple similar people, we keep the highest rating
                        if book_name not in recommended_books or rating_value >recommended_books[book_name] :## check if the book exist in the books that the user ratings
                            recommended_books[book_name]=rating_value

    #  Sort the results based on the rating (the value)
    # .items() turns the dictionary into a list of pairs so we can sort them
    # key=lambda x: x[1] is used to sort by the rating, not the name
    # reverse=True  to put the highest ratings (5s) at the very top

    sorted_list = sorted(recommended_books.items(), key=lambda x: x[1], reverse=True)


    return sorted_list





# this function help the user to see the statistiques of each book
# (matplotlib.org, n.d.)
#(GeeksforGeeks, 2024)
def book_visualization(data):

    # if the data is empty, don't try to draw a graph
    if  not  data:
        print("No data available to visualize.")
        return
    
    total_ratings={}     # This empty dictionary to store the total ratings of books  
    books_count={}            # This empty dictionary to count how many times the book was rated

    for The_user_name in data:   # looping through each user
        for book_name in data[The_user_name]: # looping through the rated books by the each user
            rating=data[The_user_name][book_name]
            if book_name not in  total_ratings:         #check if the book does not exist in the total 
                total_ratings[book_name]=0              # this initialization for the book appears for the first time in the data
                books_count[book_name]=0
            total_ratings[book_name]+=rating             # to calculate the total ratings of books
            books_count[book_name]+=1                    # counting  how many times the books  has been rated

    The_avg_ratings={}                 # creating an empty dictionary to store the average of the ratings of books
    for book_name in total_ratings:    #loop through each book in total ratings of the dictionary
        The_avg_ratings[book_name]=total_ratings[book_name]/books_count[book_name]    # calculating the average

    sorted_books=sorted(The_avg_ratings.keys())      ## sort the books name alphabetically
    books=[]                   # to store book names
    ratings=[]                # to store books ratings        
    for book_name in sorted_books: # looping through the sorted books 
        books.append(book_name)     #add each book  to the books list
        ratings.append(books_count[book_name]) # add the average rating of books to the rating list
    
    positions=range(len(books))           # to create the position of each book in the graph
    plt.bar(positions, ratings, color='skyblue', edgecolor='navy')# # draws bars by using x and y  axis and rotate  label for better readability
    plt.xticks(positions,books,rotation=45,ha='right') # Replace X-axis numbers with book names and rotate 45 degrees to prevent overlapping
    plt.xlabel("books in data")                         # label the x axis with as
    plt.ylabel("Number of Readers")                          #label the y axis with as
    plt.title("Book recommendation statistics")                         # the title of the graph 
    plt.tight_layout()                  #To show that  the book names aren't cut off at the bottom
    plt.show()                              # to show the final graph 

   

    # this function that call back the functions that i used before to run the code
#(docs.python.org, n.d.)
def main():
            
        create_file()
        data=read_data()
        user_rating={}
        #get the user name
        while True:
                # Check if name is empty or consists only of numbers to prevent errors
                The_user_name = input("Welcome! Please enter your name: ")
            
                if The_user_name.strip() == "":
                    print("Name cannot be empty. Try again.")
                elif The_user_name.isdigit():
                    print("Name cannot be numbers only. Try again.")
                else:
                    print(f"\nHello, {The_user_name}!")
                    break
            
        # MENU
        while True:
            print("\n--- Main Menu ---")
            print("1. Rate random books")
            print("2. Get my recommendations")
            print("3. Show popularity graph")   
            print("4. Exit")
        
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                random_books = select_random_books(data)
                # This calls the  function to get the ratings dictionary
                print("\nPlease rate these books (1-5):")
                user_rating = collect_ratings(random_books)
                if The_user_name not in data:
                    data[The_user_name] = {}
                for book, rate in user_rating.items():
                     data[The_user_name][book] = rate
                print("Ratings saved :)!")
               
            elif choice == "2":
                if not user_rating:
                    print("!! Please rate books first (Option 1).")
                else:
                    # Calculate how similar this user is to others in the database
                    similarity = find_similar_users(data, user_rating)
                    # Generate sorted list of books based on similar tastes
                    recommendations = books_recommendation(data, similarity, user_rating)
                
                    if recommendations:
                        print("\n" + "="*30)
                        print("  TOP RECOMMENDATIONS for you  ")
                        print("="*30)
                        for book_name, rating_value in recommendations:
                            print(f" {book_name} | Predicted Rating: {rating_value}/5")
                        print("="*30)
                    else:
                       print("\nNo new recommendations found. Try rating more books!")
            elif choice == "3":
                book_visualization(data)

            elif choice == "4":
                print(f"\nThank you for using the system. Goodbye, {The_user_name}!")
                break
        
if __name__ == "__main__":
        main()
          
















    
        










    