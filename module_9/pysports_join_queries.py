# Title: pysports_join queries.py
#Author: Allison Partch
#Date: 11 February 2023
#Test program to execute joining players and team tables in pysport database

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

try:
    #connecting to pysports database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    #inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    #get results from cursor
    players = cursor.fetchall()
    print("\n -- DISPLAYING PLAYER RECORDS --")

    #select from player table
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))
    input("\n\n Press any key to continue...")

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