# Title: what_a_book.py
#Author: Allison Partch
#Date: 22 February 2023
#Description: WhatABook program

#import statements
import sys
import mysql.connector
from mysql.connector import errorcode

#config database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# show_menu
def show_menu():
    print("\n -- Main Menu --")
    print("     1. View Books\n     2. View Store Locations\n     3. My Account\n     4. Exit Program")

    try:
        choice = int(input('    <Example enter: 1 for book listings>: '))
        return choice

    except ValueError:
        print("\n Invalid number, program terminated...\n") 
        sys.exit(0)

# show book
def show_book(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()
    print("\n -- DISPLAYING BOOK LISTING --")
    
    # data sets and display results
    for book in books:
        print(" Book Name: {}\n Author: {}\n Details: {}\n".format(book[1], book[2], book[3]))

# show locations
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()
    print("\n -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print(" Locale: {}\n".format(location[1]))

# validate users IDs
def validate_user():
    try:
        user_id = int(input('\n Enter a customer id <Example 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n Invalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id

    except ValueError:
        print("\n Invalid number, program terminated....\n")
        sys.exit(0)

# show account menu to user
def show_account_menu():
    try:
        print("\n   -- Customer Menu --")
        print("     1. Wishlist\n     2. Add Book\n     3. Main Menu")
        account_option = int(input('    <Example enter: 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\n Invalid number, program terminated...\n")
        sys.exit(0) 

#query database for list of books to users wishlist
def show_wishlist(_cursor, _user_id):
    
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

    wishlist = _cursor.fetchall()
    print("\n -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("     Book Name: {}\n     Author: {}\n".format(book[4], book[5]))

# query the database for list of books not in users wishlist 
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()
    print("\n -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("     Book Id: {}\n       Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    # try/catch block for errors within MySQL 

    #connecting to whatabook database within MySQL
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    print("\n Welcome to the WhatABook Application! ")

    #show main menu
    user_selection = show_menu()

    #user selection not is not 4 
    while user_selection != 4:

        # if user selects 1, call show_book
        if user_selection == 1:
            show_book(cursor)
        #if user selects 2, call show_location
        if user_selection == 2:
            show_locations(cursor)
        #if user selects 3, call validate_user to validate user and call show_account_menu for account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu() 
            
            #account options does not equal 3 
            while account_option != 3:
                #if user selects 1, call show_wishlist of user
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                #if user selects 2, call show_books_to_add not in users wishlist
                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)

                    #book_id input from user 
                    book_id = int(input("\n Enter id of the book you want to add: "))

                    #add book to users wishlist 
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    #commit to database of changes 
                    db.commit()
                    print("\n   Book id: {} was added to your wishlist!".format(book_id))

                # dislay invalid option if input is less than 0 or greater than 3 
                if account_option < 0 or account_option > 3:
                    print("\n Invalid option, please retry...")

                #show account menu
                account_option = show_account_menu()

        #display invalid option if input is less than 0 or greater than 4 
        if user_selection < 0 or user_selection > 4:
            print("\n   Invalid option, please retry...")

        #show main menu
        user_selection = show_menu() 

    print("\n\n Program terminated...")                   

except mysql.connector.Error as err:
    """ handle errors """   
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
        """ close the connection to MySQL"""
        db.close()


