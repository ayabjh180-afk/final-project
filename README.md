APP NAME
Book recomendation system
GitHub Repository URL:
https://github.com/ayabjh180-afk/final-project.git


Identification:
- Name: aya boujhayne
- P-number: P470421
- Course code: IY 499


Declaration of Own Work:
I confirm that this assignment is my own work.
Where I have referred to academic sources, I have provided proper in-text citations and included the sources in the final reference list.

Introduction:

This project implements a Book Recommendation  and Data Analysis System using the Matplotlib and CSV libraries.The application  enables users to rate books and receive personalized recommendations based on similarities with other users.


The main functionality of the app includes:

- Personilized Rating system: users rate a selection of  books to create their own preference profil.
- Recommendation based on similiraity:Applies a similarity algorithm to identify users with comparable preference and generate book recommendations.
- Statiscal visualisation:  Features a bar chart that displays book popularity based on the number of  readers for each title of book


Installation:
To run the app locally:
1. Make sure Python 3.12 is installed.
2. Install required dependencies:
   pip install pygame

How to Run the App:
1. Open terminal/command prompt in the project folder.
2. Run the main script:
   python "project up.py"
3. Controls:
   - Menu:Type a number from 1 to 4 and press Enter to select:
   1: Rate random books .
   2: Get my recommendations .
   3: Show popularity graph .
   4: Exit .
   - Inputting Ratings:Type a number between 1 and 5 when prompted to rate a book.
   - Graph Window: The chart is presented in a separate pop-up window. Once the window is closed, the user is returned to the terminal interface.

App Elements:
- CSV File : The program reads from and writes to a file called book_ratings.csv to store user data for later use.
-Recommendation System: The program compares user ratings to find similar users and suggest books they might like.
-Input Validation: The program checks user input to make sure names and ratings are valid and prevents errors.

Libraries Used:
- Matplotlib: Helps draw a graph of book ratings.
- CSV: Saves and loads the book data.
- Random: Chooses random books so the user sees different ones each time.

Project Structure:
ProjectFolder/
├── project_up.py:The main file that runs the program and contains all the code.
├── book_ratings.csv : The database  file that  stores all the book titles, usernames, and ratings           
├── requirements.txt:requirements.txt: Lists the required library (matplotlib).
└── README.txt :Contains the project report and explanation.         

Testing:

- Valid Cases:    Entering numbers 1-4 navigates the menu correctly.
                  Entering ratings 1-5 saves data to the CSV successfully.
- Invalid Cases:  Entering "1234" as a name is blocked by the system.
                  Entering "6" as a rating triggers a "Try again" message instead of a crash.
- Boundary Cases: Entering exactly "1" or "5" works perfectly.
                  Choosing "Recommendations" before rating any books displays a helpful warning message.


References:
Brett, M. (2020). Storing and loading text: Coding for Data. [online] Matthew-brett.github.io. Available at: https://matthew-brett.github.io/cfd2020/wild-pandas/text_encoding.html [Accessed 10 Apr. 2026].

GeeksforGeeks (2024). Sorting Algorithms in Python. [online] Available at: https://www.geeksforgeeks.org/sorting-algorithms/ [Accessed 10 Apr. 2026].

Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), pp. 90-95.

Matplotlib Development Team (2024). Pyplot tutorial — Matplotlib 3.8.0 documentation. [online] Available at: https://matplotlib.org/stable/tutorials/pyplot.html [Accessed 10 Apr. 2026].

Python Software Foundation (2020). csv — CSV File Reading and Writing. [online] Available at: https://docs.python.org/3/library/csv.html [Accessed 10 Apr. 2026].

Python Software Foundation (2023). main — Top-level code environment. [online] Available at: https://docs.python.org/3/library/main.html [Accessed 10 Apr. 2026].

Python Software Foundation (2025). random — Generate pseudo-random numbers. [online] Available at: https://docs.python.org/3/library/random.html [Accessed 10 Apr. 2026].

Python Software Foundation (2026). io — Core tools for working with streams. [online] Available at: https://docs.python.org/3/library/io.html [Accessed 10 Apr. 2026].

Python Software Foundation (2026). More Control Flow Tools: Lambda Expressions. [online] Available at: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions [Accessed 10 Apr. 2026].

Real Python (2024). Python Exceptions: An Introduction. [online] Available at: https://realpython.com/python-exceptions/ [Accessed 10 Apr. 2026].

Real Python (2025). How to Use Python Lambda Functions. [online] Available at: https://realpython.com/python-lambda/ [Accessed 10 Apr. 2026].

Real Python (2025). Reading and Writing CSV Files in Python. [online] Available at: https://realpython.com/python-csv/ [Accessed 10 Apr. 2026].

Real Python (2025). Unicode & Character Encodings in Python. [online] Available at: https://realpython.com/python-encodings-guide/ [Accessed 10 Apr. 2026].

W3Schools (2026). Python int() Function. [online] Available at: https://www.w3schools.com/python/ref_func_int.asp [Accessed 10 Apr. 2026].

W3Schools (2026). Python Dictionaries and Lambda Functions. [online] Available at: https://www.w3schools.com/python/python_dictionaries.asp [Accessed 10 Apr. 2026].