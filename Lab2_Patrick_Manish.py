# Lab 2 Group 1
# Patrick Hollyer-Viggiani and Manish Singh
# Test Case Design
# February 11, 2024
# Decription: Create a program that allows for the user to store book data in a csv file, allow the data that is stored to be 
#             permanent until deleted by user.  Additionally, the user can select to add a book, search for a book, or end the program.

# Importing csv functionality
import csv

# Asigning books.csv to a constant 'BOOK_FILE'
BOOK_FILE = "books.csv"

#'book_add' function that allows user to add the title, author, and year for a book
def book_add(title:str, author:str , year:int):
    # .strip method to remove any extra spaces from the title and author
    title=title.strip()
    author=author.strip()
    # Opens the csv file in append mode, newline to ensure no empty lines
    with open (BOOK_FILE, 'a', newline="") as file:
        # Creates a writer in csv file
        writer = csv.writer(file)
        # Creates a new row within writer to add title author and year
        writer.writerow([title, author, year])
    # Print out the title, author, and year that the user inputed        
    print(f"Added: {title} by {author} published in {year} to your reading list.")
    
# 'list_books' function to display the books
def list_books():
    # Opens the csv file in read mode
    with open(BOOK_FILE, "r",) as file:
        # Creates a csv reader object
        reader = csv.reader(file)
        # Creates a flag that checks if books are in the csv file, defaults to false
        books_in_reader = False
        # For loop that iterates through the csv and prints the index number and row value. Start = 1 sets index to 1 - lets book number start at 1
        for index, row in enumerate(reader,start=1):
            # Printing the book number (index), and the title (row[0]), author (row[1]), and year (row[2]) of book
            print(f"Book #{index} - Title: {row[0]} | Author: {row[1]} | Year: {row[2]}")
            # Sets the book flag to True to signify that there are books
            books_in_reader = True
        
        # If the user has not entered any books, print the following
        if not books_in_reader:
             print("\nNo books found. Please select 'a' to add books.")

# 'search_book' function to search for certain books in the csv file 
def search_book():
    # Taking input for the book title
    title = input("\nEnter the title of the book to search: ")
    # Opens the csv file in reader mode
    with open(BOOK_FILE, "r") as file:
        # Create a csv reader object
        reader = csv.reader(file)
        # Initialize the flag to false
        book_found = False
        # For loop that goes through each row in the csv file
        for row in reader:
            # If there are any matches, add it too search_keyword list, accounting converting to lower to account for user inputs
            if row[0].lower() == title.lower():
                # Print the corresponding title, author, and year of pupblication for the book. Row 0 = title, 1 = author, and 2 = publication year
                print(f"\nBook found with the title: {row[0]}\nThe author of book is: {row[1]}\nThe year of publication is: {row[2]}")
                # Sets the flag to True
                book_found = True
                # Breaks the loop
                break
        # If the book could not be found, prints an error message
        if not book_found:
            print(f"\nThe book '{title}' was not found.")

                
# While loop to initalize the process for inputs
while True:
    # Input statement, asking user to enter a, b, c, or d to complete options - input is converted to lower to account for user putting capitals
    option = input(f"\na) Add a book.\nb) Display list of books.\nc) Search for a book.\nd) End the program.\nPlease select an option: ").lower()
    # Condition with input prompt to add a book to the csv file, prompting for title, author, and publication year
    if option == "a":
        title = input("\nPlease enter the book's title: ")
        author = input("Please enter the author's name: ")
        year = input("Please enter the book's year of publication: ")
        
        # Error message if invalid publication year input
        if not year.isdigit():
            print("\nPlease ensure year of publication is valid. Try Again.")
            
        # If valid input add to csv file, ensuring year is int
        else:
            book_add(title, author, int(year))
            
    # Condition with input prompt to view the current list of books in csv file
    elif option == "b":
        list_books()
        
    # Condition with input prompt to the current list of books based on title
    elif option == "c":  
        search_book()
      
    # Condition with input prompt to end the program
    elif option == "d":
        quit()
        
    # If invalid input, display the following and prompt for input again
    else:
        print("Please enter a valid option between a-d.")