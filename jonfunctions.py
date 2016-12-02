import random
#
#
import pypyodbc
#https://code.google.com/archive/p/pypyodbc/wikis/A_HelloWorld_sample_to_access_mssql_with_python.wiki
#
#

class jonfunctions:
    def newBlackCard(bigBlackDeck):#draws a new black card from the deck
        if len(bigBlackDeck) > 0:
            return bigBlackDeck.pop(random.randrange(0, len(bigBlackDeck)))
        else:
            jonfunctions.error("flaccidblackdeck")#error, bigBlackDeck array is empty

    def error(errorCode):#takes error codes and displays appropriate message
        if errorCode == "flaccidblackdeck":#error, bigBlackDeck array is empty
            print("no cards present in black deck")#possible to be replaced with message on game screen

    def arrayDropVar(targetArr, dropVar):#purge all instances of specific value from array, always call with pos at 0
        newArr = []
        for x in len(targetArr):
            if targetArr[x] != dropVar:
                newArr.append(dropVar)
        return newArr

    def dbConnect(queries):
        dbConn = pypyodbc.connect('!!!PUT DATABASE HERE!!!')
        cur = dbConn.cursor()
        for x in len(queries):
            cur.execute(queries[x])
        funcReturn = []
        for row in cur.fetchall():
            funcReturn.append(row)
        cur.close()
        dbConn.close()
        return funcReturn