# Title: pysports_join queries.py
#Author: Allison Partch
#Date: 11 February 2023
#Test program to execute inserting, updating, and deleting records from pysport database

#import statements
import mysql.connector
from mysql.connector import errorcode

#config database
config = {
    "user": "pysports_user",
    "password": "Titan312",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):
    #inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    #get results from cursor
    players = cursor.fetchall()
    print("\n -- {} --".format(title))
    #display the results of player
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    #connect to pysport database
    db = mysql.connector.connect(**config)

    #get cursor
    cursor = db.cursor()

    #insert a player in data
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    player_data = ("Shawn", "White", 1)
    cursor.execute(add_player, player_data)

    #commit the insert to database
    db.commit()
    #show all records in player table
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #update the new player
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Shawn'")
    #execute update
    cursor.execute(update_player)
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #delete player
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(delete_player)
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n Press any key to continue... ")

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