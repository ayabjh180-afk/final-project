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


def ratingsave(user_name, book_name, rating_value):
    """Save one new rating to the file."""
    try:
        file = open(DATA_FILE, "a", newline="")
        writer = csv.writer(file)
        writer.writerow([user_name, book_name, rating_value])
        file.close()
    except:
        print("Could not save data.")


def get_books(data):
    """Get all books."""
    books = []

    for user in data:
        for book in data[user]:
            if book not in books:
                books.append(book)

    return books


def show_books(data):
    """Print all books."""
    books = get_books(data)

    print("\nBooks:")
    for book in books:
        print("-", book)


def search_book(data):
    """Search for a book."""
    word = input("Enter a word: ").strip().lower()
    books = get_books(data)
    found = False

    for book in books:
        if word in book.lower():
            print("-", book)
            found = True

    if found == False:
        print("No books found.")


def show_popular(data):
    """Show how many times each book was rated."""
    counts = {}

    for user in data:
        for book in data[user]:
            if book not in counts:
                counts[book] = 0
            counts[book] = counts[book] + 1

    print("\nPopular books:")
    for book in counts:
        print(book, "-", counts[book], "ratings")


def get_user_input_ratings(data):
    """Ask the user to rate three random books."""
    books = get_books(data)

    if len(books) == 0:
        return {}

    if len(books) <= 3:
        chosen = books
    else:
        chosen = random.sample(books, 3)

    new_ratings = {}

    print("\nRate these books from 1 to 5.\n")

    for book in chosen:
        while True:
            answer = input(book + ": ").strip()

            try:
                value = int(answer)

                if value >= 1 and value <= 5:
                    new_ratings[book] = value
                    break
                else:
                    print("Enter a number from 1 to 5.")

            except ValueError:
                print("Enter a valid number.")

    return new_ratings


def find_recommendations(new_ratings, data):
    """
    Recommend books using a simple idea:
    find users who rated the same books similarly,
    then collect other books they liked.
    """
    scores = {}

    for user in data:
        same = 0

        for book in new_ratings:
            if book in data[user]:
                difference = abs(new_ratings[book] - data[user][book])

                if difference <= 1:
                    same = same + 1

        if same >= 2:
            for book in data[user]:
                if book not in new_ratings:
                    if book not in scores:
                        scores[book] = 0

                    scores[book] = scores[book] + data[user][book]

    best_books = []

    for book in scores:
        best_books.append((book, scores[book]))

    best_books.sort(reverse=True)

    return best_books


def recommendation_part(data):
    """Run the recommendation feature."""
    name = input("Enter your name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    ratings = get_user_input_ratings(data)

    if len(ratings) == 0:
        print("No ratings entered.")
        return

    for book in ratings:
        save_rating(name, book, ratings[book])

    print("\nRecommended books:")
    results = find_recommendations(ratings, data)

    if len(results) == 0:
        print("No recommendations found.")
    else:
        count = 0
        for item in results:
            print("-", item[0])
            count = count + 1
            if count == 5:
                break


def menu():
    """Show the menu."""
    print("\nBOOK PROGRAM")
    print("1. Show all books")
    print("2. Search for a book")
    print("3. Show popular books")
    print("4. Get recommendations")
    print("5. Exit")


def main():
    create_file()
    data = load_data()

    while True:
        menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            show_books(data)

        elif choice == "2":
            search_book(data)

        elif choice == "3":
            show_popular(data)

        elif choice == "4":
            recommendation_part(data)

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


main()