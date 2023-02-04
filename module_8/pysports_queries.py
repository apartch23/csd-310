# Title: pysports_join queries.py
#Author: Allison Partch
#Date: 04 February 2023
#Test program to execute queries against pysport database

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

# try/catch database errors
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
#select from team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
#get results from cursor oject
    teams = cursor.fetchall()
    print("\n -- DISPLAYING TEAM RECORDS --")    

    for team in teams:
        print("Team ID: {}\n Team Name: {}\n Mascot: {}\n".format(team[0], team[1], team[2]))

#select from player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")
    players = cursor.fetchall()
    print("\n -- DISPLAYING PLAYER RECORDS --")  

    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

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
