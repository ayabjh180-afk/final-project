# ============================================
# #########   BOOK PROGRAM  #################
# ============================================

import math
import random

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

DATA_FILE = "book_ratings.csv"


def create_file_if_missing():
    """Create starter CSV data if the file does not exist."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            file.read(1)
    except FileNotFoundError:
        starter_data = [
            ["user", "book", "rating"],
            ["Alice", "Dune", "5"],
            ["Alice", "1984", "4"],
            ["Alice", "The Hobbit", "5"],
            ["Bob", "Dune", "4"],
            ["Bob", "1984", "5"],
            ["Bob", "The Catcher in the Rye", "3"],
            ["Charlie", "Brave New World", "5"],
            ["Charlie", "The Great Gatsby", "4"],
            ["Charlie", "1984", "2"],
            ["Diana", "The Hobbit", "5"],
            ["Diana", "Pride and Prejudice", "5"],
            ["Diana", "Dune", "4"],
            ["Ethan", "1984", "5"],
            ["Ethan", "Brave New World", "4"],
            ["Ethan", "The Catcher in the Rye", "2"],
            ["Fatima", "The Alchemist", "5"],
            ["Fatima", "Dune", "4"],
            ["George", "The Great Gatsby", "5"],
            ["George", "1984", "4"],
        ]

        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(starter_data)


def load_data():
    """Load CSV data into a nested dictionary."""
    data = {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if "user" not in row or "book" not in row or "rating" not in row:
                    continue

                user = row["user"].strip()
                book = row["book"].strip()

                if user == "" or book == "":
                    continue

                try:
                    rating = float(row["rating"])
                except ValueError:
                    continue

                if rating < 1 or rating > 5:
                    continue

                if user not in data:
                    data[user] = {}

                data[user][book] = rating

    except FileNotFoundError:
        print("Data file not found.")
    except Exception as error:
        print("Error while loading file:", error)

    return data


def save_all_data(data):
    """Rewrite the whole CSV file using current dictionary data."""
    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["user", "book", "rating"])

            for user in data:
                for book in data[user]:
                    writer.writerow([user, book, data[user][book]])
    except Exception:
        print("Could not save the file.")


def get_all_books(data):
    """Return all unique books sorted alphabetically."""
    books = []

    for user in data:
        for book in data[user]:
            if book not in books:
                books.append(book)

    books.sort()
    return books


def similarity(user_ratings, other_ratings):
    """
    Compare two users using cosine similarity.
    The code is simple, but the logic is smart because
    it compares rating patterns instead of just averages.
    """
    common_books = []

    for book in user_ratings:
        if book in other_ratings:
            common_books.append(book)

    if len(common_books) == 0:
        return 0

    top = 0
    bottom1 = 0
    bottom2 = 0

    for book in common_books:
        top += user_ratings[book] * other_ratings[book]
        bottom1 += user_ratings[book] ** 2
        bottom2 += other_ratings[book] ** 2

    if bottom1 == 0 or bottom2 == 0:
        return 0

    return top / (math.sqrt(bottom1) * math.sqrt(bottom2))


def find_best_match(new_user, data):
    """Find the most similar user in the dataset."""
    best_name = ""
    best_score = -1

    for user in data:
        score = similarity(new_user, data[user])

        if score > best_score:
            best_score = score
            best_name = user

    return best_name, best_score


def recommend_books(new_user, data):
    """
    Recommend unread books using weighted scores.
    Books from more similar users have more influence.
    """
    scores = {}
    totals = {}

    for user in data:
        score = similarity(new_user, data[user])

        if score <= 0:
            continue

        for book in data[user]:
            if book not in new_user:
                if book not in scores:
                    scores[book] = 0
                    totals[book] = 0

                scores[book] += data[user][book] * score
                totals[book] += score

    results = []

    for book in scores:
        predicted = scores[book] / totals[book]
        results.append((book, predicted))
    #(W3Schools, 2019)
    results.sort(key=lambda item: item[1], reverse=True)
    return results


def search_books(data):
    """Search for books by keyword."""
    word = input("Enter a keyword: ").strip().lower()
    books = get_all_books(data)
    found = False

    for book in books:
        if word in book.lower():
            print("-", book)
            found = True

    if not found:
        print("No books found.")


def show_popular_books(data):
    """Show books sorted by number of ratings."""
    counts = {}
    totals = {}

    for user in data:
        for book in data[user]:
            if book not in counts:
                counts[book] = 0
                totals[book] = 0

            counts[book] += 1
            totals[book] += data[user][book]

    result = []

    for book in counts:
        average = totals[book] / counts[book]
        result.append((book, counts[book], average))

    result.sort(key=lambda item: (item[1], item[2]), reverse=True)

    print("\nPopular books:")
    for item in result:
        print(f"{item[0]} | ratings: {item[1]} | average: {item[2]:.2f}")


def get_valid_rating():
    """Ask for a rating from 1 to 5 or Enter to skip."""
    while True:
        answer = input("Enter rating from 1 to 5 (or press Enter to skip): ").strip()

        if answer == "":
            return None

        try:
            value = float(answer)
            if 1 <= value <= 5:
                return value
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")


def get_user_ratings(data):
    """Ask the user to rate random books."""
    books = get_all_books(data)

    if len(books) < 5:
        chosen_books = books
    else:
        chosen_books = random.sample(books, 5)

    ratings = {}

    print("\nRate some books.\n")

    for book in chosen_books:
        print(book)
        value = get_valid_rating()
        if value is not None:
            ratings[book] = value

    return ratings


def show_user_ratings(name, data):
    """Display one user's ratings."""
    if name not in data or len(data[name]) == 0:
        print("This user has no ratings.")
        return

    print("\nYour ratings:")
    for book in sorted(data[name]):
        print(f"{book} -> {data[name][book]}")


def edit_user_rating(name, data):
    """Allow a user to add or change one rating."""
    if name not in data:
        data[name] = {}

    books = get_all_books(data)

    print("\nAvailable books:")
    for book in books:
        print("-", book)

    chosen_book = input("\nType the exact book name: ").strip()

    if chosen_book == "":
        print("Book name cannot be empty.")
        return

    value = get_valid_rating()

    if value is None:
        print("No rating entered.")
        return

    data[name][chosen_book] = value
    save_all_data(data)
    print("Rating saved.")


def delete_user_rating(name, data):
    """Allow a user to delete one of their ratings."""
    if name not in data or len(data[name]) == 0:
        print("You have no ratings to delete.")
        return

    show_user_ratings(name, data)
    chosen_book = input("\nType the exact book name to delete: ").strip()

    if chosen_book in data[name]:
        del data[name][chosen_book]
        save_all_data(data)
        print("Rating deleted.")
    else:
        print("That book was not found in your ratings.")


def save_new_user(name, ratings, data):
    """Save or update the user's ratings in memory and file."""
    data[name] = ratings
    save_all_data(data)


def plot_popularity_chart(data):
    """Plot a basic popularity chart if matplotlib is installed."""
    if plt is None:
        print("Matplotlib is not installed.")
        print("Install it with: pip install matplotlib")
        return

    counts = {}
    for user in data:
        for book in data[user]:
            if book not in counts:
                counts[book] = 0
            counts[book] += 1

    items = []
    for book in counts:
        items.append((book, counts[book]))

    items.sort(key=lambda item: item[1], reverse=True)
    items = items[:5]

    if len(items) == 0:
        print("No data to show.")
        return

    book_names = []
    rating_counts = []

    for item in items:
        book_names.append(item[0])
        rating_counts.append(item[1])

    plt.figure(figsize=(10, 5))
    plt.bar(book_names, rating_counts)
    plt.title("Top 5 Most Popular Books")
    plt.xlabel("Books")
    plt.ylabel("Number of Ratings")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()


def show_all_books(data):
    """Display all books."""
    books = get_all_books(data)
    print("\nAll books:")
    for book in books:
        print("-", book)


def recommendation_menu(name, data):
    """Sub-menu for user profile actions."""
    while True:
        print("\nUSER MENU")
        print("1. Show my ratings")
        print("2. Add or change one rating")
        print("3. Delete one rating")
        print("4. Get recommendations")
        print("5. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            show_user_ratings(name, data)

        elif choice == "2":
            edit_user_rating(name, data)

        elif choice == "3":
            delete_user_rating(name, data)

        elif choice == "4":
            if name not in data or len(data[name]) < 2:
                print("Please make sure you have at least 2 ratings first.")
                continue

            match_name, match_score = find_best_match(data[name], data)
            books = recommend_books(data[name], data)

            print(f"\nMost similar user: {match_name} ({match_score:.3f})")
            print("\nRecommended books:")

            if len(books) == 0:
                print("No recommendations found.")
            else:
                for item in books[:5]:
                    print(f"{item[0]} | predicted rating: {item[1]:.2f}")

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def menu():
    """Main menu."""
    print("\nBOOK RECOMMENDER")
    print("1. Show all books")
    print("2. Search books")
    print("3. Show popular books")
    print("4. Create profile and rate books")
    print("5. Open my user menu")
    print("6. Show popularity chart")
    print("7. Exit")


def main():
    create_file_if_missing()
    data = load_data()
    current_user = ""

    while True:
        menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            show_all_books(data)

        elif choice == "2":
            search_books(data)

        elif choice == "3":
            show_popular_books(data)

        elif choice == "4":
            name = input("Enter your name: ").strip()

            if name == "":
                print("Name cannot be empty.")
                continue

            new_user = get_user_ratings(data)

            if len(new_user) < 2:
                print("Please rate at least 2 books.")
                continue

            save_new_user(name, new_user, data)
            current_user = name
            print("Profile created and ratings saved.")

        elif choice == "5":
            if current_user == "":
                current_user = input("Enter your user name: ").strip()

            if current_user == "":
                print("Name cannot be empty.")
                continue

            if current_user not in data:
                data[current_user] = {}
                save_all_data(data)

            recommendation_menu(current_user, data)

        elif choice == "6":
            plot_popularity_chart(data)

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


main()