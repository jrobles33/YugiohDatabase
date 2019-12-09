import sqlite3
import os.path

#Initial Database connection - Need absolute path to connect to the same database
BASE_DIR = os.path.dirname(os.path.abspath("C:/Documents/CSE111/Project/Yugioh.db"))
db_path = os.path.join(BASE_DIR, "Yugioh.db")
db_connection = None  # connection to the database, empty for now
db_name = "C:\\Documents\\CSE111\\Project\\Yugioh.db"  # exact path to database
item = 100
try:
    db_connection = sqlite3.connect(db_name)
except sqlite3.Error as err:
    print(err)
LogIn = False
#This function searches for Monster Cards based on Name
def MCard_Search(searchCursor):
    with sqlite3.connect("Yugioh.db") as db:
        if(searchCursor == 1):
            searchVariable = "m_name"
            searchBy = "Name"
        if(searchCursor == 2):
            searchVariable = "m_cardID"
            searchBy = "Card ID"
        if(searchCursor == 3):
            searchVariable = "m_attribute"
            searchBy = "Attribute"
        if(searchCursor == 4):
            searchVariable = "m_type"
            searchBy = "Type"
        if(searchCursor == 5):
            searchBy = "Attack"
            searchVariable = "m_attack"
        if(searchCursor == 6):
            searchBy = "Defense"
            searchVariable = "m_defense"
        if(searchCursor == 7):
            searchBy = "Effect"
            searchVariable = "m_effect"
        if(searchCursor == 8):
            searchBy = "Level"
            searchVariable = "m_level"
        if(searchCursor == 9):
            searchBy = "Sacrifices Needed"
            searchVariable = "m_sacrifice"
        curs = db.cursor()
        monsName = raw_input("\nEnter " + searchBy+ ": \n")
        if (searchVariable == "m_attack" or searchVariable == "m_defense"):
            greaterOrLess = input("\nPress 1 for Greater, Press 2 for Less\n")
            if (greaterOrLess == 1):
                query = ("SELECT * FROM Monster Where " +searchVariable +" >= " + monsName )
            if (greaterOrLess == 2):
                query = ("SELECT * FROM Monster Where " +searchVariable +" <= " + monsName )
        else:
            query = ("SELECT * FROM Monster WHERE " +searchVariable +" like '%" + monsName + "%'")
        curs.execute(query)
        mons = curs.fetchall()
        for row in mons:
            print(str("Name: " + str(row[0]) + " | Card ID: " + str(row[1]) + " | Attribute: " + str(
                row[2]) + " | Type: " + str(row[3]) + " | Attack: " + str(row[4]) + " | Defense: " + str(
                row[5]) + " | Effect: " + str(row[6]) + " | Level: " + str(row[7]) + " | Sacrifices Needed: " + str(
                row[8]) + "\n"))

#This function searches for Trap Cards based on Name
def TCard_Search(searchCursor):
    with sqlite3.connect("Yugioh.db") as db:
        if(searchCursor == 1):
            searchVariable = "t_name"
            searchBy = "Name"
        if(searchCursor == 2):
            searchVariable = "t_cardID"
            searchBy = "Card ID"
        if(searchCursor == 3):
            searchVariable = "t_type"
            searchBy = "Type"
        if(searchCursor == 4):
            searchVariable = "t_effect"
            searchBy = "Effect"
        curs = db.cursor()
        trapName = raw_input("\nEnter " + searchBy+ ": \n")
        query = ("SELECT * FROM Trap WHERE "+ searchVariable +" like '%" + trapName + "%'")
        curs.execute(query)
        traps = curs.fetchall()
        for row in traps:
            print("Name: " + str(row[0]) + " | Card ID: " + str(row[1]) + " | Type: " + str(
                row[2]) + " | Effect: " + str(row[3]) + "\n")

#This function searches for Spell Cards based on Name
def SCard_Search(searchCursor):
    with sqlite3.connect("Yugioh.db") as db:
        if(searchCursor == 1):
            searchVariable = "s_name"
            searchBy = "Name"
        if(searchCursor == 2):
            searchVariable = "s_cardID"
            searchBy = "Card ID"
        if(searchCursor == 3):
            searchVariable = "s_type"
            searchBy = "Attribute"
        if(searchCursor == 4):
            searchVariable = "s_effect"
            searchBy = "Effect"
        curs = db.cursor()
        spellName = raw_input("\nEnter " + searchBy+ ": \n")
        query = ("SELECT * FROM Spell WHERE "+ searchVariable +" like '%" + spellName + "%'")
        curs.execute(query)
        spells = curs.fetchall()
        for row in spells:
            print("Name: " + str(row[0]) + " | Card ID: " + str(row[1]) + " | Type: " + str(
                row[2]) + " | Effect: " + str(row[3]) + "\n")

#This function searches for Spell Cards based on Name
def Deck_Search():
    with sqlite3.connect("Yugioh.db") as db:
        curs = db.cursor()
        DeckName = raw_input("\nEnter Name: \n")
        query = ("SELECT * FROM Contains WHERE d_name like '%" + DeckName + "%' ORDER BY d_name desc")
        curs.execute(query)
        Decks = curs.fetchall()
        for row in Decks:
            print("Deck Name: " + str(row[0]) + " | Card Name: " + str(row[1]) + " | Card ID: " + str(
                row[2]) + "\n")

def MonsterSearch():
    searchCursor = input("\nHow would you like to search?\n\nPress 1 to search by Name, 2 by ID, 3 by Attribute, 4 by Type, 5 by Attack, 6 by Defense, 7 by Effect, 8 by Level, 9 by Sacrifice:\n")
    MCard_Search(searchCursor)

def TrapSearch():
    searchCursor = input("\nHow would you like to search?\n\nPress 1 to search by Name, 2 by ID, 3 by Type, 4 by Effect\n")
    TCard_Search(searchCursor)

def SpellSearch():
    searchCursor = input("\nHow would you like to search?\n\nPress 1 to search by Name, 2 by ID, 3 by Type, 4 by Effect\n")
    SCard_Search(searchCursor)

def updateDeckAdd(usernameEnter, cardNameOrID):
        #We are inputting the card Name
        with sqlite3.connect("Yugioh.db") as db:
            curs = db.cursor()
            query = ("INSERT INTO Contains VALUES((SELECT d_name FROM Decks WHERE d_owner = '" + usernameEnter +"'), '"+ cardNameOrID+ "', (SELECT c_cardID FROM Cards WHERE c_name = '"+ cardNameOrID+"')) ")
            curs.execute(query)

def updateDeckRem(usernameEnter, cardNameOrID):
    with sqlite3.connect("Yugioh.db") as db:
        curs = db.cursor()
        query = ("DELETE FROM Contains where c_name = '"+ cardNameOrID +"' and d_name = (SELECT d_name from Decks where d_owner = '" + usernameEnter + "')")
        curs.execute(query)



def updateDeck(usernameEnter):
    DeckCursor = input("\nPress 1 to Add Cards, Press 2 to Remove Cards\n")
    cardNameOrID = raw_input("\nPlease Enter Card Name: \n")
    if (DeckCursor == 1):
        updateDeckAdd(usernameEnter, cardNameOrID)
    if (DeckCursor == 2):
        updateDeckRem(usernameEnter, cardNameOrID)

def LoggedInUser(usernameEnter):
    logInSelect = input("\n\nWelcome " + usernameEnter + ". What would you like to do?\nPress 1 to update Deck, press 2 to edit Personal Info.\n")
    if(logInSelect == 1):
        updateDeck(usernameEnter)
    # if(logInSelect == 2):
    #     updateInfo(usernameEnter)


def UserLogin():
    usernameEnter = raw_input("\nPlease enter your Username\n")
    with sqlite3.connect("Yugioh.db") as db:
        curs = db.cursor()
        query = ("Select p_username FROM Players where p_username like '" + usernameEnter + "'")
        curs.execute(query)
        UN = curs.fetchall()
        for row in UN:
            if (str(row[0]) == usernameEnter):
                LoggedInUser(usernameEnter)

def UserRegister():
    print ("test")



def UserEnter():
    searchCursor = input("\nPress 1 to Log in or 2 to Sign up.\n")
    if (searchCursor == 1):
        UserLogin()
    if (searchCursor == 2):
        UserRegister()

def adminAddorDel(selectionA, selectionB):
    with sqlite3.connect("Yugioh.db") as db:
        curs = db.cursor()
        if(selectionA == 1):
                if(selectionB == 1):
                    monName = raw_input("\nPlease enter Monster Name:\n")
                    monID = raw_input("\nPlease enter Card ID:\n")
                    monAttr = raw_input("\nPlease enter Monster Attribute:\n")
                    monType = raw_input("\nPlease enter Monster Type:\n")
                    monAttack = raw_input("\nPlease enter Monster Attack:\n")
                    monDefense = raw_input("\nPlease enter Monster Defense:\n")
                    monEffect = raw_input("\nIs it an effect monster? Press 1 for Yes, 2 for No:\n")
                    monLevel = raw_input("\nPlease enter Monster Level:\n")
                    monSacrifices = raw_input("\nPlease enter how many sacrifices are needed:\n")
                    query = ("INSERT INTO Monster VALUES('"+monName+"', '"+monID+"', '"+monAttr+"', '"+monType+"', "+monAttack+", "+monDefense+", "+monEffect+", "+monLevel+", "+monSacrifices+")")
                    curs.execute(query)
                    #add monster
                if(selectionB == 2):
                    #add spell
                    spellName = raw_input("\nPlease enter Spell Name:\n")
                    spellID = raw_input("\nPlease enter Card ID:\n")
                    spellType = raw_input("\nPlease enter Spell Type:\n")
                    spellEff = raw_input("\nPlease enter Spell Effect:\n")
                    query = ("INSERT INTO Spell VALUES('"+spellName+"', '"+spellID+"', '"+spellType+"', '"+spellEff+"')")
                    curs.execute(query)
                if(selectionB == 3):
                    #add trap
                    tName = raw_input("\nPlease enter Trap Name:\n")
                    tID = raw_input("\nPlease enter Card ID:\n")
                    tType = raw_input("\nPlease enter Trap Type:\n")
                    tEff = raw_input("\nPlease enter Trap Effect:\n")
                    query = ("INSERT INTO Trap VALUES('"+tName+"', '"+tID+"', '"+tType+"', '"+tEff+"')")
                    curs.execute(query)
        if(selectionA == 2):
            CardName = raw_input("\nPlease Enter Card Name:\n")
            query = ("DELETE FROM Cards WHERE c_name = '"+CardName+"'")
            curs.execute(query)




def AdminMode():
    selectionA = input("\nPress 1 to add cards, Press 2 to delete cards\n")
    selectionB = input("\nPress 1 for Monster Cards, 2 for Spell Cards, 3 for Trap Cards\n")
    adminAddorDel(selectionA, selectionB)


#Start of Output, will cycle through START: for as long as the user wants
db_connection = sqlite3.connect(db_name)

print("\nWelcome to the Yugioh Database: What would you like to do? \n\n")
#START:
while True:
    if item == 100:
        item = input("\nPress 1 to search the database, Press 2 to log in, Press 3 to Enter Admin Mode.\n")
        if (item == 1):
            print("\nWhat would you like to search for?")
            selection = input("\nPress 1 to search for Cards, Press 2 to search for Decks, Press 0 to return to Main Screen.\n")
            if(selection == 0):
                item = 100
            if(selection == 1):
                CardSearch = input("\nPress 1 to search for Monster Cards, Press 2 to search for Trap Cards, Press 3 to search for Spell Cards, Press 0 to return to Main Screen.\n")
                if (CardSearch == 1):
                    MonsterSearch()
                    item = 100
                if(CardSearch == 2):
                    TrapSearch()
                    item = 100
                if(CardSearch == 3):
                    SpellSearch()
                    item = 100
                if(CardSearch == 0):
                    item = 100
            if(selection == 2):
                Deck_Search()
                item = 100
        if (item == 2):
                UserEnter()
                item = 100

        if (item == 3):
            AdminMode()
            item = 100
