#main running file for Cards Against Humanity pycharm game
import player
import card
import jonfunctions as jon

class main:
    gameState = "menu" #identifies current game state:
    #menu = user is in the starting menu
    #lobby = user is in the game lobby, ready to enter a game
    #newroom = user wants to create a new game room
    #newround = a new round is starting, used to prep game for new round
    #qna = a question is being asked and players are answering
    #choice = all answers have been entered and the asking player is choosing the winning entry
    #gameend = the game has ended, scores are tallied
    #quit = user has chosen to quit the game

    userState = [](str)#identifies the state of the user, variable is array so user can be in more than 1 state at a time
    #ask = user is asking a question, currently choosing the winning answer
    #answer = user is answering a question, after answering player state goes to "wait"
    #wait = user is waiting, either the player is asking a question and is waiting for players to answer or player has answered and is waiting for the asker to decide on a winner
    #leave = user chooses to leave game

    drawArr = [](str)#array of what parts of the game need to be drawn on screen
    roundPos = 0#the current round position in the game, from 0 to however many players are in the game
    bigBlackDeck = [](card)#the deck holding the black cards. the deck is really big and really black
    players = [](player)#array of players in the user's game, used for drawing the game. to be populated by the server
    blackCard = None(card)#current black/question card in play
    whiteField = [](card)#array of white cards that have been submitted to answer question/black card
    userId = 0#temporary value, user will be assigned an ID by the server
    clickEvents = ""#what the player clicked on

    #
    #main game loop
    #
    while gameState != "quit":

        #clickEvents = getClickEvents()
        #fetch what the player clicked on from the UI

        #drawBase(gameState) #tells the screen drawer to draw a background appropriate for current game state
        #function wil go live when drawing system is ready

        if gameState == "qna" or gameState == "choice":
            # checks to see if certain values are present in array, then calls the appropriate functions with appropriate values
            if "question" in drawArr:#calls draw function to draw current question on screen
                todo = True
                #drawBlack(blackCard)
            if "qnew" in drawArr:
                todo = True
                #if newBlack(blackCard):
                #   arrayDropVar(drawArr, "qnew", 0)
            if len(whiteField) > 0:
                for x in range(0, len(whiteField)):
                    todo = True
                    #drawWhite(whiteField[x], x)
                    #sends draw call for a white card as well as the index of the card (for positioning)
            #drawHand(players[userId].playerHand)#draws the player's hand

        if "commitanswer" in clickEvents:#when a player chooses to commit their answer(s) that players state changes to "wait"
            userState = "wait"

        #send an sql query to the database to add a point to the player who played the winning answer
        #"confirmwinner" can only be added to clickevents if the player playing on local machine was selecting answers
        if "confirmwinner" in clickEvents:
            dbQuery = []
            dbQuery.append("!!!GIVE WINNING PLAYER POINTS IN DB!!!")
            dbQuery.append("!!!ROTATE ROUND!!!")#add query to call function to rotate round
            ignorethistmp = jon.dbConnect(dbQuery) #reference won't work for some bizarre reason
            #FETCH NEW ROUND POSITION FROM DB DATA
            gameState = "newround"

        if gameState == "newround":
            dbQuery = []
            dbQuery.append("!!!FETCH GAME STATS!!!")#fetch game stats from server (scores, round position etc)
            ignorethistmp = jon.dbConnect(dbQuery)
