import sqlite3
import os.path

#Initial Database connection - Need absolute path to connect to the same database
BASE_DIR = os.path.dirname(os.path.abspath("D:/Schoolwork/CSE111/Phase3/Yugioh.db"))
db_path = os.path.join(BASE_DIR, "Yugioh.db")
db_connection = None  # connection to the database, empty for now
db_name = "D:\\Schoolwork\\CSE111\\Phase3\\Yugioh.db"  # exact path to database
item = 100
try:
    db_connection = sqlite3.connect(db_name)
except sqlite3.Error as err:
    print(err)

#This function searches for Monster Cards based on Name
def MCard_Search():
    with sqlite3.connect("Yugioh.db") as db:
        curs = db.cursor()
        monsName = raw_input("\nEnter card: \n")
        query = ("SELECT * FROM Monster WHERE m_name like '%" + monsName + "%'")
        curs.execute(query)
        mons = curs.fetchall()
        for row in mons:
            print(str("Name: " + str(row[0]) + " | Card ID: " + str(row[1]) + " | Attribute: " + str(
                row[2]) + " | Type: " + str(row[3]) + " | Attack: " + str(row[4]) + " | Defense: " + str(
                row[5]) + " | Effect: " + str(row[6]) + " | Level: " + str(row[7]) + " | Sacrifices Needed: " + str(
                row[8]) + "\n"))

#This function searches for Trap Cards based on Name
def TCard_Search():
    with sqlite3.connect("Yugioh.db") as db:
        curs = db.cursor()
        trapName = raw_input("\nEnter card: \n")
        query = ("SELECT * FROM Trap WHERE t_name like '%" + trapName + "%'")
        curs.execute(query)
        traps = curs.fetchall()
        for row in traps:
            print(str(row))

#This function searches for Spell Cards based on Name
def SCard_Search():
    with sqlite3.connect("Yugioh.db") as db:
        curs = db.cursor()
        spellName = raw_input("\nEnter card: \n")
        query = ("SELECT * FROM Spell WHERE s_name like '%" + spellName + "%'")
        curs.execute(query)
        spells = curs.fetchall()
        for row in spells:
            print(str(row))

#This function searches for Spell Cards based on Name
def Deck_Search():
    with sqlite3.connect("Yugioh.db") as db:
        curs = db.cursor()
        DeckName = raw_input("\nEnter Name: \n")
        query = ("SELECT * FROM Contains WHERE d_name like '%" + DeckName + "%'")
        curs.execute(query)
        Decks = curs.fetchall()
        for row in Decks:
            print(str(row))


#Start of Output, will cycle through START: for as long as the user wants
db_connection = sqlite3.connect(db_name)
print("\nWelcome to the Yugioh Database: What would you like to do? \n\n")
#START:
while True:
    if item == 100:
        item = input("\nPress 1 to search the database, Press 2 to log in, Press 3 enter admin mode\n")
        if (item == 1):
            print("\nWhat would you like to search for?")
            selection = input("\nPress 1 to search for Cards, Press 2 to search for Decks, Press 3 to search for Players, Press 0 to return to Main Screen.\n")
            if(selection == 0):
                item = 100
            if(selection == 1):
                CardSearch = input("\nPress 1 to search for Monster Cards, Press 2 to search for Trap Cards, Press 3 to search for Spell Cards, Press 0 to return to Main Screen.\n")
                if (CardSearch == 1):
                    MCard_Search()
                    item = 100
                if(CardSearch == 2):
                    TCard_Search()
                    item = 100
                if(CardSearch == 3):
                    SCard_Search()
                    item = 100
                if(CardSearch == 0):
                    item = 100
            if(selection == 2):
                Deck_Search()
                item = 100
        if (item == 2):
            print("\nWe are logging in now")
        if (item == 3):
            print("\nWe are in admin mode")
