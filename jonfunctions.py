import random, json as j, urllib.request as u, pprint, pypyodbc as p
#
#
#
#
#######





urlCAHdb = "http://tsuts.tskoli.is/2t/2202903449/CAH_JSON/anotherCAHjsonDB.json"

reponseCAH = u.urlopen(urlCAHdb).read()

dataCAH = j.loads(reponseCAH.decode('utf-8'))


## trying pretty print ##

pp = pprint.PrettyPrinter(indent=4, depth=6)

#pp.pprint(dataCAH)



#Get randomm number


for row in dataCAH:
    #print(row)
    countCards = +1

#print(countCards)


#######

bigBlackDeck = []

tinyWhiteDeck = []

sortDeckCounter = 0


while(sortDeckCounter != 2953):

    #GET THE CARD TYPE
    cardType = dataCAH[sortDeckCounter]['cardType']
    #CHECK IF WHITE OR BLACK CARDS
    if(cardType == 'A' and sortDeckCounter < 2953):
        tinyWhiteDeck.append(dataCAH[sortDeckCounter]['text'])
        #print("whitecard: " + tinyWhiteDeck)
        sortDeckCounter = sortDeckCounter +1
    elif(cardType == 'Q' and sortDeckCounter < 2953):
        bigBlackDeck.append(dataCAH[sortDeckCounter]['text'])
        #print("blackcard: " + bigBlackDeck)
        sortDeckCounter = sortDeckCounter + 1







userTinyWhiteDeck = []
userCardsCount = 0

flaccidCards = []


while(userCardsCount < 10):
    getRandom = random.randrange(0, 2333)
    if getRandom not in flaccidCards:
        userTinyWhiteDeck.append(tinyWhiteDeck[getRandom])
        userCardsCount = userCardsCount + 1
        flaccidCards.append(getRandom)
    else:
        #print("OH SHIT IS A DITTO")
        continue



#for card in userTinyWhiteDeck:












#STILL NOT SURE WHAT THE BELOW CODE IS FOR EXACTLY

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
        #THIS IS DATABASE I UPLOADED STILL HAVENET USED IT!
        dbConn = p.connect(host='tsuts.tskoli.is', port=3306, user='2202903449', passwd='mypassword', db='2202903449_cah')
        cur = dbConn.cursor()
        for x in len(queries):
            cur.execute(queries[x])
        funcReturn = []
        for row in cur.fetchall():
            funcReturn.append(row)
        cur.close()
        dbConn.close()
        return funcReturn